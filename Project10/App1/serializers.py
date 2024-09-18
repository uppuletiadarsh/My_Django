# myapp/serializers.py
from rest_framework import serializers
from .models import Employee
from rest_framework import viewsets

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

"""


"""