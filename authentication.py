import jwt
from datetime import datetime, timedelta
from django.conf import settings

class JWTAuth:
    @staticmethod
    def generate_token(user):
        expiration_time = datetime.utcnow() + timedelta(minutes=60)
        payload = {'user_id': user.id, 'exp': expiration_time}
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
