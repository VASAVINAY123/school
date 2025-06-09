"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from teacher import views as teacher
from student import views as student
from school import views as school

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',teacher.hello),
    #path('home/',teacher.home,name='home'),
    path('index/',school.index,name='index'),
    path('admin1/',school.adminlogin,name='admin1'),
    path('adminloginentered/',school.adminloginentered,name='adminloginentered'),
    path('activatestudent/',student.activatestudent,name='activatestudent'),
    #path('activateteacher/',teacher.activateteacher,name='activateteacher'),
    path('logout/',school.logout,name='logout'),


    path('teacher/',teacher.teacherlogin,name='teacher'),
    path('teacherpage/',teacher.teacherpage,name='teacherpage'),
    path('tchrregister/',teacher.tchrregister,name='tchrregister'),
    path('teacherlogincheck/',teacher.teacherlogincheck,name='teacherlogincheck'),
    path('teacherclass/',teacher.teacherclass,name='teacherclass'),
    path('tweek1/',teacher.tweek1,name='tweek1'),
    path('tweek2/',teacher.tweek2,name='tweek2'),
    path('tweek3/',teacher.tweek3,name='tweek3'),
    path('tweek4/',teacher.tweek4,name='tweek4'),
    path('tweek5/',teacher.tweek5,name='tweek5'),
    path('tweek6/',teacher.tweek6,name='tweek6'),
    path('tweek7/',teacher.tweek7,name='tweek7'),
    path('tweek8/',teacher.tweek8,name='tweek8'),
    path('tweek9/',teacher.tweek9,name='tweek9'),
    path('tweek10/',teacher.tweek10,name='tweek10'),
    path('tweek11/',teacher.tweek11,name='tweek11'),
    path('tweek12/',teacher.tweek12,name='tweek12'),
    path('tweek2class1/',teacher.tweek2class1,name='tweek2class1'),
    path('tweek3class1/',teacher.tweek3class1,name='tweek3class1'),
    path('tweek4class1/',teacher.tweek4class1,name='tweek4class1'),
    path('tweek5class1/',teacher.tweek5class1,name='tweek5class1'),
    path('tweek6class1/',teacher.tweek6class1,name='tweek6class1'),
    path('tweek7class1/',teacher.tweek7class1,name='tweek7class1'),
    path('tweek8class1/',teacher.tweek8class1,name='tweek8class1'),
    path('tweek9class1/',teacher.tweek9class1,name='tweek9class1'),
    path('tweek10class1/',teacher.tweek10class1,name='tweek10class1'),
    path('tweek11class1/',teacher.tweek11class1,name='tweek11class1'),
    path('tweek12class1/',teacher.tweek12class1,name='tweek12class1'),
    path('class1/',teacher.class1,name='class1'),
    path('tclass2week2/',teacher.tclass2week2,name='tclass2week2'),
    path('tweek2class/',teacher.tweek2class,name='tweek2class'),
    path('tweek3class2/',teacher.tweek3class2,name='tweek3class2'),
    path('tweek4class2/',teacher.tweek4class2,name='tweek4class2'),
    path('tweek5class2/',teacher.tweek5class2,name='tweek5class2'),
    path('tweek6class2/',teacher.tweek6class2,name='tweek6class2'),
    path('tweek7class2/',teacher.tweek7class2,name='tweek7class2'),
    path('tweek8class2/',teacher.tweek8class2,name='tweek8class2'),
    path('tweek9class2/',teacher.tweek9class2,name='tweek9class2'),
    path('tweek10class2/',teacher.tweek10class2,name='tweek10class2'),
    path('tweek11class2/',teacher.tweek11class2,name='tweek11class2'),
    path('tweek12class2/',teacher.tweek12class2,name='tweek12class2'),
    path('studentsolutions/',teacher.studentsolutions,name='studentsolutions'),
    path('finalscore/',teacher.finalscore,name='finalscore'),


    #path('teacherdetails/',teacher.teacherdetails,name='teacherdetails'),




    path('student/',student.studentlogin,name='student'),
    path('studentpage/',student.studentpage,name='studentpage'),
    path('studentregister/',student.studentregister,name='studentregister'),
    path('studentlogincheck/',student.studentlogincheck,name='studentlogincheck'),
    path('studentloginche/',student.studentlogincheck,name='studentlogincheck'),
    path('studentdetails/',student.studentdetails,name='studentdetails'),
    path('studentclass/',student.studentclass,name='studentclass'),
    path('week/',student.week,name='week'),
    path('week2/',student.week2,name='week2'),
    path('week3/',student.week3,name='week3'),
    path('week4/',student.week4,name='week4'),
    path('week5/',student.week5,name='week5'),
    path('week6/',student.week6,name='week6'),
    path('week7/',student.week7,name='week7'),
    path('week8/',student.week8,name='week8'),
    path('week9/',student.week9,name='week9'),
    path('week10/',student.week10,name='week10'),
    path('week11/',student.week11,name='week11'),
    path('week12/',student.week12,name='week12'),
    path('sweek1class1/',student.sweek1class1,name='sweek1class1'),
    path('sweek1class2/',student.sweek1class2,name='sweek1class2'),
    path('sweek2class2/',student.sweek2class2,name='sweek2class2'),
    path('sweek3class2/',student.sweek3class2,name='sweek3class2'),
    path('sweek4class2/',student.sweek4class2,name='sweek4class2'),
    path('sweek5class2/',student.sweek5class2,name='sweek5class2'),
    path('sweek6class2/',student.sweek6class2,name='sweek6class2'),
    path('sweek7class2/',student.sweek7class2,name='sweek7class2'),
    path('sweek8class2/',student.sweek8class2,name='sweek8class2'),
    path('sweek9class2/',student.sweek9class2,name='sweek9class2'),
    path('sweek10class2/',student.sweek10class2,name='sweek10class2'),
    path('sweek11class2/',student.sweek11class2,name='sweek11class2'),
    path('sweek12class2/',student.sweek12class2,name='sweek12class2'),
    path('practise1/',student.practise1,name='practise1'),
    path('class2solution1/',student.class2solution1,name='class2solution1'),
    path('class2solution2/',student.class2solution2,name='class2solution2'),
    path('class2solution3/',student.class2solution3,name='class2solution3'),
    path('class2solution4/',student.class2solution4,name='class2solution4'),
    path('class2solution5/',student.class2solution5,name='class2solution5'),
    path('class2solution6/',student.class2solution6,name='class2solution6'),
    path('class2solution7/',student.class2solution7,name='class2solution7'),
    path('class2solution8/',student.class2solution8,name='class2solution8'),
    path('class2solution9/',student.class2solution9,name='class2solution9'),
    path('class2solution10/',student.class2solution10,name='class2solution10'),
    path('class2solution11/',student.class2solution11,name='class2solution11'),
    path('class2solution12/',student.class2solution12,name='class2solution12'),
    path('studentscore/',student.studentscore,name='studentscore'),
    # path('stdclass1/',student.stdclass1,name='stdclass1'),
    #path('class2/',student.class2,name='class2')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
