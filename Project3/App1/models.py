from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    eid = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    domain = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    