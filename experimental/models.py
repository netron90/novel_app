from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    wallet=models.PositiveIntegerField(default=0)
    pass
