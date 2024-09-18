from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=20,null=True)  # Make sure this field is defined correctly
    Empid = models.IntegerField(primary_key=True)  # IntegerField should not have max_length
    Domain = models.CharField(max_length=20)