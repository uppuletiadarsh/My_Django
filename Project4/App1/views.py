from django.shortcuts import render
from . models import Employee
# Create your views here.
def register(req):
    return render(req,'register.html')
def save(req):
    if req.method=="POST":
        name = req.POST['ename']
        eid = req.POST['eid']
        salary = req.POST['sal']
        save = Employee(ename=name,eid = eid,salary=salary)
        save.save()
    return render(req,'success.html')
def det(request):
    if request.method=="POST":
        det = Employee.objects.all()
    return render(request,'success.html',{'det':det})
