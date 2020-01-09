from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.TextField(default='')
    body=models.TextField(default='')
    year=models.CharField(max_length=10)
    month=models.CharField(max_length=5)
    day=models.CharField(max_length=5)
    reason=models.TextField(default='')