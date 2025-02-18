from django.contrib.auth.models import Group
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add your app name here
]
DEBUG = False  # Keep this False for production

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'your-domain.com']  # Add your domain here
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
