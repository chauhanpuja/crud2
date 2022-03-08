from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User_Data(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

