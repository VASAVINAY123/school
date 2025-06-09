from django.db import models

# Create your models here.

class tchr(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    qualification = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='teacheregister'


class fileupload(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload'


class fileupload2(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload2'


class fileupload3(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload3'


class fileupload4(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload4'

class fileupload5(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload5'


class fileupload6(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload6'


class fileupload7(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload7'

class fileupload8(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload8'

class fileupload9(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload9'


class fileupload10(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload10'

class fileupload11(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload11'


class fileupload12(models.Model):
    filename = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'fileupload12'

#class2
class classupload1(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload1'

class classupload2(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload2'

class classupload3(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload3'

class classupload4(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload4'

class classupload5(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload5'

class classupload6(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload6'

class classupload7(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload7'

class classupload8(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload8'

class classupload9(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload9'

class classupload10(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload10'

class classupload11(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload11'

class classupload12(models.Model):
    topic = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/pdfs/')
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.topic

    class Meta:
        db_table = 'classupload12'


class finalscoremodel(models.Model):
    week = models.CharField(max_length=100, default="", editable=True)
    email = models.CharField(max_length=100, default="", editable=True)
    task = models.CharField(max_length=100)
    solution = models.CharField(max_length=50)
    marks=models.CharField(max_length=50)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='finalscore'






