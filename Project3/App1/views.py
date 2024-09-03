from django.shortcuts import render
from .models import Employee

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        salary = request.POST['sal']
        eid = request.POST['eid']
        domain = request.POST['dom']
        position = request.POST['pos']
        Emp = Employee(name=name,salary=salary,eid=eid,domain=domain,position=position)
        Emp.save()
    return render(request,'home.html')