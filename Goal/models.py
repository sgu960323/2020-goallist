from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    writer=models.TextField(default='')
    title=models.TextField(default='')
    body=models.TextField(default='')
    year=models.CharField(max_length=10)
    month=models.CharField(max_length=5)
    day=models.CharField(max_length=5)
    reason=models.TextField(default='')
    subject=models.TextField(default='')