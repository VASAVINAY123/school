from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='studentregister'


class userssolution1(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution1'

class userssolution2(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution2'

class userssolution3(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution3'

class userssolution4(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution4'

class userssolution5(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution5'

class userssolution6(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution6'

class userssolution7(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution7'

class userssolution8(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution8'

class userssolution9(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution9'

class userssolution10(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution10'

class userssolution11(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution11'

class userssolution12(models.Model):
    week = models.CharField(max_length=100,default="", editable=True)
    email = models.CharField(max_length=100,default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userssolution12'









