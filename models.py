from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # 👈 Add this line

    def __str__(self):
        return self.title
