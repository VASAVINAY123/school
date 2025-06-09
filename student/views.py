from django.shortcuts import render
from  student.models import *
from  student.forms import *
from django.http import HttpResponse
from django.contrib import messages
from teacher.models import *

def studentlogin(request):
    return render(request,'student/studentlogin.html')

def studentpage(request):
    return render(request,'student/studentpage.html')

def studentregister(request):
    if request.method=='POST':
        form1=studentForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, "student/studentlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=studentForm()
        return render(request,"student/studentregister.html",{"form":form})


def studentlogincheck(request):
    if request.method == 'POST':
        sname = request.POST.get('sname')
        print(sname)
        spasswd = request.POST.get('spasswd')
        print(spasswd)
        try:
            check = student.objects.get(name=sname, passwd=spasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'student/studentpage.html')
            else:
                messages.success(request, 'student is not activated')
                return render(request, 'student/studentlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'student/studentlogin.html')

def studentdetails(request):
    s=student.objects.all()
    return render(request,'admin/studentdetails.html',{"qs":s})

def activatestudent(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        student.objects.filter(id=uname).update(status=status)
        qs=student.objects.all()
        return render(request,"admin/studentdetails.html",{"qs":qs})


def studentclass(request):
    return render(request,'student/studentclass.html')

def week(request):
    return render(request,'student/week1.html')

def week2(request):
    return render(request,'student/sweek2.html')

def week3(request):
    return render(request,'student/sweek3.html')
def week4(request):
    return render(request,'student/sweek4.html')
def week5(request):
    return render(request,'student/sweek5.html')
def week6(request):
    return render(request,'student/sweek6.html')
def week7(request):
    return render(request,'student/sweek7.html')
def week8(request):
    return render(request,'student/sweek8.html')
def week9(request):
    return render(request,'student/sweek9.html')
def week10(request):
    return render(request,'student/sweek10.html')
def week11(request):
    return render(request,'student/sweek11.html')
def week12(request):
    return render(request,'student/sweek12.html')

def sweek1class1(request):
    filedata = fileupload.objects.all()
    return render(request,'student/sweek1class1.html',{'object':filedata})

def sweek1class2(request):
    object = classupload1.objects.all()
    return render(request,'student/sweek1class2.html',{'object':object})

def sweek2class2(request):
    object = classupload2.objects.all()
    return render(request,'student/sweek2class2.html',{'object':object})

def sweek3class2(request):
    object = classupload3.objects.all()
    return render(request,'student/sweek3class2.html',{'object':object})
def sweek4class2(request):
    object = classupload4.objects.all()
    return render(request,'student/sweek4class2.html',{'object':object})
def sweek5class2(request):
    object = classupload5.objects.all()
    return render(request,'student/sweek5class2.html',{'object':object})
def sweek6class2(request):
    object = classupload6.objects.all()
    return render(request,'student/sweek6class2.html',{'object':object})
def sweek7class2(request):
    object = classupload7.objects.all()
    return render(request,'student/sweek7class2.html',{'object':object})
def sweek8class2(request):
    object = classupload8.objects.all()
    return render(request,'student/sweek8class2.html',{'object':object})
def sweek9class2(request):
    object = classupload9.objects.all()
    return render(request,'student/sweek9class2.html',{'object':object})
def sweek10class2(request):
    object = classupload10.objects.all()
    return render(request,'student/sweek10class2.html',{'object':object})
def sweek11class2(request):
    object = classupload11.objects.all()
    return render(request,'student/sweek11class2.html',{'object':object})
def sweek12class2(request):
    object = classupload12.objects.all()
    return render(request,'student/sweek12class2.html',{'object':object})


def practise1(request):
    return render(request,'student/class2.html')


def class2solution1(request):
    if request.method=='POST':
        form1=userssolution1Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution1Form()
        return render(request,"student/class2.html",{'form':form})

def class2solution2(request):
    if request.method=='POST':
        form1=userssolution2Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution2Form()
        return render(request,"student/p2class2.html",{'form':form})

def class2solution3(request):
    if request.method=='POST':
        form1=userssolution3Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution3Form()
        return render(request,"student/p3class2.html",{'form':form})

def class2solution4(request):
    if request.method=='POST':
        form1=userssolution4Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution4Form()
        return render(request,"student/p4class2.html",{'form':form})

def class2solution5(request):
    if request.method=='POST':
        form1=userssolution5Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution5Form()
        return render(request,"student/p5class2.html",{'form':form})


def class2solution6(request):
    if request.method=='POST':
        form1=userssolution6Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution6Form()
        return render(request,"student/p6class2.html",{'form':form})

def class2solution7(request):
    if request.method=='POST':
        form1=userssolution7Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution7Form()
        return render(request,"student/p7class2.html",{'form':form})

def class2solution8(request):
    if request.method=='POST':
        form1=userssolution8Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution8Form()
        return render(request,"student/p8class2.html",{'form':form})

def class2solution9(request):
    if request.method=='POST':
        form1=userssolution9Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution9Form()
        return render(request,"student/p9class2.html",{'form':form})

def class2solution10(request):
    if request.method=='POST':
        form1=userssolution10Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution10Form()
        return render(request,"student/p10class2.html",{'form':form})


def class2solution11(request):
    if request.method=='POST':
        form1=userssolution11Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution11Form()
        return render(request,"student/p11class2.html",{'form':form})


def class2solution12(request):
    if request.method=='POST':
        form1=userssolution12Form(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            return render(request, "student/studentpage.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form = userssolution12Form()
        return render(request,"student/p12class2.html",{'form':form})

def studentscore(request):
    final=finalscoremodel.objects.all()
    return render(request,'student/studentscore.html',{"object":final})



