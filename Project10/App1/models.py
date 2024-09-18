from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    domain = models.CharField(max_length=40)
    company = models.CharField(max_length=40)