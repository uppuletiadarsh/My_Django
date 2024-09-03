from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    physics = models.PositiveIntegerField(primary_key=True)
    chemistry = models.PositiveIntegerField()
    english = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField() 