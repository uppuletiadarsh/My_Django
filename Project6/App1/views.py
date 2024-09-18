from django.shortcuts import render,get_object_or_404
from . models import Employee
# Create your views here.
def home(request):
    return render(request,'home.html')

def save(request):
    if request.method =='POST':
        name = request.POST['name']
        empid = request.POST['empid']
        salary = request.POST['salary']
        name = request.POST['name']
        domain = request.POST['domain']
        role = request.POST['role']
        e = Employee(name= name , empid=empid,salary=salary,domain=domain,role=role)
        e.save()
        return render(request,'home.html')
def details(request):
    det = Employee.objects.all()
    return render(request,'details.html',{'det':det})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def update(request,id):
    details = Employee.objects.get(empid=id)
    return render(request,'update.html',{'det':details})
def updated(request,id):
    details = Employee.objects.get(empid=id)
    name = request.POST['name']
    empid = request.POST['empid']
    salary = request.POST['salary']
    name = request.POST['name']
    domain = request.POST['domain']
    role = request.POST['role']
    details.empid = empid
    details.name = name
    details.salary = salary
    details.domain = domain
    details.role = role
    details.save()
    return redirect('details')

def delete(request,id):
    details = Employee.objects.get(empid=id)
    details.delete()
    return redirect('details')



"""
class Employee(models.Model):
    empid = models.CharField(primary_key=True,max_length=10)  
    name = models.CharField(max_length=20)  
    salary = models.IntegerField()  
    domain = models.CharField(max_length=20) 
    role = models.CharField(max_length=20)  
"""