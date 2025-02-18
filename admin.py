from django.contrib import admin
from .models import User, Quiz, Question, QuizAttempt, QuizResponse

admin.site.register(User)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(QuizAttempt)
admin.site.register(QuizResponse)
