from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    empid = models.CharField(primary_key=True,max_length=10)  
    name = models.CharField(max_length=20)  
    salary = models.IntegerField()  
    domain = models.CharField(max_length=20) 
    role = models.CharField(max_length=20)  

    