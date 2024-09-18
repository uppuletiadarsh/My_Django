from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)