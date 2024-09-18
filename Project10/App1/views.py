from django.shortcuts import render
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def employee(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmpSerializer(employees, many=True)
        return Response({'employees': serializer.data})

    if request.method == 'POST':
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'employee': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Employee
from .serializers import EmpSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Employee
from .serializers import EmpSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Employee
from .serializers import EmpSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def employee_id(request, id):
    # Fetch the employee instance
    employee = get_object_or_404(Employee, pk=id)

    if request.method == 'GET':
        # Handle GET request: Retrieve and return employee data
        serializer = EmpSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Handle PUT request: Update the employee data
        serializer = EmpSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Handle DELETE request: Delete the employee
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



