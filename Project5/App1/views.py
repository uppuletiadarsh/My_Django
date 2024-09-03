from django.shortcuts import render
from . models import Student
# Create your views here.
def students(request):
    
    return render(request,'students.html',)
def save(req):
    if req.method == "POST":
        htno = req.POST['rno']
        name = req.POST['Name']
        ph = int(req.POST['ph'])
        ch = int(req.POST['ch'])
        eng = int(req.POST['eng'])
        total = float(ph + ch + eng)
        details = Student(roll_no=htno, name=name, physics=ph, chemistry=ch, english=eng,total_marks=total)
        details.save()
        message = 'Data Entered SuccessFully'
        return render(req,'students.html',{'m':message})
    
def det(request):
    det = Student.objects.all()
    return render(request,'details.html',{'det':det})