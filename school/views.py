from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',{})

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def logout(request):
    return render(request, "index.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")


