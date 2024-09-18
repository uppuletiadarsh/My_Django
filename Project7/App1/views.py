

from django.shortcuts import render, get_object_or_404
from .models import Employee



def home(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'create':
            Name = request.POST.get('Name')
            Empid = request.POST.get('Empid')
            Domain = request.POST.get('Domain')
            e = Employee(Name=Name, Empid=Empid, Domain=Domain)
            e.save()
        elif action == 'update':
            emp_id = request.POST.get('Empid')
            e = get_object_or_404(Employee, Empid=emp_id)
            e.Domain = request.POST.get('Domain')
            e.Name = request.POST.get('Name')
            e.save()
        elif action == 'delete':
            emp_id = request.POST.get('Empid')
            e = get_object_or_404(Employee, Empid=emp_id)
            e.delete()
    data = Employee.objects.all()
    return render(request, 'home.html', {'data': data})


