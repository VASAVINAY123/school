from django.shortcuts import render
from teacher.models import tchr
from student.models import *
from teacher.forms import *
from django.http import HttpResponse
from django.contrib import messages


def hello(request):
    return render(request,'hello.html')



def teacherpage(request):
    return render(request,'teacher/teacherpage.html')


def teacherlogin(request):
    return render(request,"teacher/teacherlogin.html")

# def teacher(request):
#     return render(request,'teacher/teacherregister.html')

def tchrregister(request):
    if request.method=='POST':
        form1=tchrForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, "teacher/teacherlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=tchrForm()
        return render(request,"teacher/teacherregister.html",{"form":form})


def teacherlogincheck(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        if uname == 'Teacher' and passwd == 'Teacher@2020':
            return render(request, "teacher/teacherpage.html")
        else:
            messages.success(request, 'Invalid name and password')
            return render(request, 'teacher/teacherlogin.html')
    return render(request, "teacher/teacherlogin.html")



def teacherclass(request):
    return render(request,"teacher/teacherclass.html")

def tweek1(request):
    return render(request,"teacher/tweek1.html")

def class1(request):
    if request.method == 'POST':
        form = fileuploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek1.html')
    else:
        form = fileuploadForm()
    return render(request,'teacher/class1.html',{'form': form})

def tweek2(request):
    return render(request,"teacher/tweek2.html")

def tweek2class1(request):
    if request.method == 'POST':
        form = fileuploadForm2(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek2.html')
    else:
        form =fileuploadForm2()
    return render(request,'teacher/tweek2class1.html',{'form':form})

def tweek3(request):
    return render(request,"teacher/tweek3.html")

def tweek3class1(request):
    if request.method == 'POST':
        form = fileuploadForm3(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek3.html')
    else:
        form =fileuploadForm3()
    return render(request,'teacher/tweek3class1.html',{'form':form})

def tweek4(request):
    return render(request,"teacher/tweek4.html")

def tweek4class1(request):
    if request.method == 'POST':
        form = fileuploadForm4(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek4.html')
    else:
        form =fileuploadForm4()
    return render(request,'teacher/tweek4class1.html',{'form':form})

def tweek5(request):
    return render(request,"teacher/tweek5.html")

def tweek5class1(request):
    if request.method == 'POST':
        form = fileuploadForm5(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek5.html')
    else:
        form =fileuploadForm5()
    return render(request,'teacher/tweek5class1.html',{'form':form})



def tweek6(request):
    return render(request,"teacher/tweek6.html")
def tweek6class1(request):
    if request.method == 'POST':
        form = fileuploadForm6(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek6.html')
    else:
        form =fileuploadForm6()
    return render(request,'teacher/tweek6class1.html',{'form':form})


def tweek7(request):
    return render(request,"teacher/tweek7.html")
def tweek7class1(request):
    if request.method == 'POST':
        form = fileuploadForm7(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek7.html')
    else:
        form =fileuploadForm7()
    return render(request,'teacher/tweek7class1.html',{'form':form})


def tweek8(request):
    return render(request,"teacher/tweek8.html")
def tweek8class1(request):
    if request.method == 'POST':
        form = fileuploadForm8(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek8.html')
    else:
        form =fileuploadForm8()
    return render(request,'teacher/tweek8class1.html',{'form':form})


def tweek9(request):
    return render(request,"teacher/tweek9.html")
def tweek9class1(request):
    if request.method == 'POST':
        form = fileuploadForm9(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek9.html')
    else:
        form =fileuploadForm9()
    return render(request,'teacher/tweek9class1.html',{'form':form})

def tweek10(request):
    return render(request,"teacher/tweek10.html")
def tweek10class1(request):
    if request.method == 'POST':
        form = fileuploadForm10(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek10.html')
    else:
        form =fileuploadForm10()
    return render(request,'teacher/tweek10class1.html',{'form':form})

def tweek11(request):
    return render(request,"teacher/tweek11.html")

def tweek11class1(request):
    if request.method == 'POST':
        form = fileuploadForm11(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek11.html')
    else:
        form =fileuploadForm11()
    return render(request,'teacher/tweek11class1.html',{'form':form})

def tweek12(request):
    return render(request,"teacher/tweek12.html")

def tweek12class1(request):
    if request.method == 'POST':
        form = fileuploadForm12(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("data saved")
            return render(request,'teacher/tweek12.html')
    else:
        form =fileuploadForm12()
    return render(request,'teacher/tweek12class1.html',{'form':form})



def tclass2week2(request):
    if request.method == 'POST':
        form = classUploadForm1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek1.html')
    else:
        form = classUploadForm1()
    return render(request, 'teacher/tclass2week2.html', {'form': form})


def tweek2class(request):
    if request.method == 'POST':
        form = classUploadForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek2.html')
    else:
        form = classUploadForm2()
    return render(request, 'teacher/tweek2class.html', {'form': form})

def tweek3class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek3.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek3class2.html', {'form': form})

def tweek4class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek4.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek4class2.html', {'form': form})

def tweek5class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek5.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek5class2.html', {'form': form})

def tweek6class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek6.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek6class2.html', {'form': form})

def tweek7class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek7.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek7class2.html', {'form': form})

def tweek8class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek8.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek8class2.html', {'form': form})

def tweek9class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek9.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek9class2.html', {'form': form})

def tweek10class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek10.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek10class2.html', {'form': form})

def tweek11class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek11.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek11class2.html', {'form': form})

def tweek12class2(request):
    if request.method == 'POST':
        form = classUploadForm3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'teacher/tweek12.html')
    else:
        form = classUploadForm3()
    return render(request, 'teacher/tweek12class2.html', {'form': form})


def studentsolutions(request):
    solutions = userssolution1.objects.all()
    return render(request, 'teacher/studentsolutions.html', {'object': solutions})
    #return render(request, 'teacher/teacherpage.html')

def finalscore(request):
    if request.method=='POST':
        week=request.POST.get('week')
        print('week',week)
        email=request.POST.get('email')
        print('email',email)
        task=request.POST.get('task')
        print("task",task)
        soultion=request.POST.get('solution')
        print('soultion',soultion)
        marks=request.POST.get('n1')
        print('marks',marks)
        finalscoremodel.objects.create(week=week,email=email,task=task,solution=soultion,marks=marks)

        solutions = userssolution1.objects.all()
        return render(request, 'teacher/studentsolutions.html', {'object': solutions})
