from django.db import models
from django.contrib.auth.models import User

class AttendancePolicy(models.Model):
    name = models.CharField(max_length=100)
    policy_document = models.FileField(upload_to='policies/')

    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.message}'
