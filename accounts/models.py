from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myuser(AbstractUser):
    name=models.TextField(default='')
    age=models.CharField(max_length=10)