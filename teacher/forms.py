from teacher.models import *
from django import forms
from django.core import validators

class tchrForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(),required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    qualification = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    def __str__(self):
        return self.mail

    class Meta:
        model=tchr
        fields=['name','passwd','cwpasswd','mail','mobileno','qualification','status']


class fileuploadForm(forms.ModelForm):

    class Meta:
        model = fileupload
        fields = ('filename','description','file')



class fileuploadForm2(forms.ModelForm):

    class Meta:
        model = fileupload2
        fields = ('filename','description','file')


class fileuploadForm3(forms.ModelForm):

    class Meta:
        model = fileupload3
        fields = ('filename','description','file')

class fileuploadForm4(forms.ModelForm):

    class Meta:
        model = fileupload4
        fields = ('filename','description','file')

class fileuploadForm5(forms.ModelForm):

    class Meta:
        model = fileupload5
        fields = ('filename','description','file')

class fileuploadForm6(forms.ModelForm):

    class Meta:
        model = fileupload6
        fields = ('filename','description','file')

class fileuploadForm7(forms.ModelForm):

    class Meta:
        model = fileupload7
        fields = ('filename','description','file')


class fileuploadForm8(forms.ModelForm):

    class Meta:
        model = fileupload8
        fields = ('filename','description','file')

class fileuploadForm9(forms.ModelForm):

    class Meta:
        model = fileupload9
        fields = ('filename','description','file')

class fileuploadForm10(forms.ModelForm):

    class Meta:
        model = fileupload10
        fields = ('filename','description','file')

class fileuploadForm11(forms.ModelForm):

    class Meta:
        model = fileupload11
        fields = ('filename','description','file')

class fileuploadForm12(forms.ModelForm):

    class Meta:
        model = fileupload12
        fields = ('filename','description','file')

#class2
class classUploadForm1(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload1
        fields = ('topic','task','file')


class classUploadForm2(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload2
        fields = ('topic','task','file')


class classUploadForm3(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload3
        fields = ('topic','task','file')

class classUploadForm4(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload4
        fields = ('topic','task','file')

class classUploadForm5(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload5
        fields = ('topic','task','file')

class classUploadForm6(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload6
        fields = ('topic','task','file')

class classUploadForm7(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload7
        fields = ('topic','task','file')

class classUploadForm8(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload8
        fields = ('topic','task','file')

class classUploadForm9(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload9
        fields = ('topic','task','file')

class classUploadForm10(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload10
        fields = ('topic','task','file')

class classUploadForm11(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload11
        fields = ('topic','task','file')

class classUploadForm12(forms.ModelForm):
    task = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    class Meta:
        model = classupload12
        fields = ('topic','task','file')

class finalscoreForm(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    marks = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    class Meta:
        model = finalscoremodel
        fields = ['week','email','task', 'solution','marks']


