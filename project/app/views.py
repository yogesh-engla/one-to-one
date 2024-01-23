
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    aadharform = Aadhar_Form()
    studentform = Student_Form()
    return render(request,'app/home.html',{'aadhar':aadharform,'student':studentform})


def add(request):
    if request.method=="POST":
        aadhar = request.POST['aadhar_no']

        data = AadharModel.objects.filter(aadhar_no=aadhar)

        if data:
            msg = "Aadhar no already exist"
            aadharform = Aadhar_Form()
            studentform = Student_Form()
            return render(request,'app/home.html',{'aadhar':aadharform,'student':studentform})
        else:
            AadharModel.objects.create(aadhar_no=aadhar)
            msg = "Aadhar no add sucessfully"
            aadharform = Aadhar_Form()
            studentform = Student_Form()
            return render(request,'app/home.html',{'aadhar':aadharform,'student':studentform})
        

def submit(request):
    if request.method == 'POST':
        stu_name = request.POST['stu_name']
        stu_address = request.POST['stu_address']
        aadhar_no = request.POST['aadhar_no']
        data = StudentModel.objects.filter(aadhar_no_id=aadhar_no)
        if data:
            msg="This aadhar no already alloted"
            aadharform = Aadhar_Form()
            studentform = Student_Form()
            return render(request,'app/home.html',{'msg':msg,'aadhar':aadharform,'student':studentform})
        else:
            data1 = AadharModel.objects.get(id=aadhar_no)
            print(data1)
            StudentModel.objects.create(stu_name=stu_name,
                                          stu_address=stu_address,
                                          aadhar_no=data1)
            msg = "Aadhar alloted successfully"
            aadharform = Aadhar_Form()
            studentform = Student_Form()
            return render(request,'app/home.html',{'msg':msg,'aadhar':aadharform,'student':studentform})