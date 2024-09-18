from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User(name=name, email=email, password=password)
            user.save()
            return render(request,'login.html')
        else:
            return render(request, 'register.html', {'error': 'Both Passwords Should be Matched'})
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = User.objects.filter(email=email)
        psw = User.objects.filter(password=password)
        
        if name and psw :  
            return render(request,'home.html',{'name':name})  
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request,'login.html')  


