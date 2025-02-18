from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Custom User Model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Add unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Add unique related_name
        blank=True
    )
# Quiz Model
class Quiz(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    num_questions = models.IntegerField()
    total_score = models.IntegerField()
    duration = models.IntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)

# Question Model
class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    options = models.JSONField()
    correct_option = models.IntegerField()
    marks = models.IntegerField()

# Quiz Attempt Model
class QuizAttempt(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('In-Progress', 'In-Progress'), ('Completed', 'Completed')], default='In-Progress')
    started_at = models.DateTimeField(default=now)
    completed_at = models.DateTimeField(null=True, blank=True)

# Response Model
class QuizResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='responses')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_option = models.IntegerField()
    correct = models.BooleanField()
    marks_awarded = models.IntegerField()
