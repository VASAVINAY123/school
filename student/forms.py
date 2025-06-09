from teacher.models import tchr
from django import forms
from student.models import *
from django.core import validators

class studentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    passwd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    cwpasswd = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    mail = forms.CharField(widget=forms.TextInput(),required=True)
    mobileno= forms.CharField(widget=forms.TextInput(), required=True, max_length=10,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(10)])
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    def __str__(self):
        return self.mail

    class Meta:
        model=student
        fields=['name','passwd','cwpasswd','mail','mobileno','status']

class userssolution1Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution1
        fields = ['week','email','task', 'solution']

class userssolution2Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution2
        fields = ['week','email','task', 'solution']

class userssolution2Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution2
        fields = ['week','email','task', 'solution']

class userssolution3Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution3
        fields = ['week','email','task', 'solution']

class userssolution4Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution4
        fields = ['week','email','task', 'solution']

class userssolution5Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution5
        fields = ['week','email','task', 'solution']

class userssolution6Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution6
        fields = ['week','email','task', 'solution']

class userssolution7Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution7
        fields = ['week','email','task', 'solution']

class userssolution8Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution8
        fields = ['week','email','task', 'solution']


class userssolution9Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution9
        fields = ['week','email','task', 'solution']


class userssolution10Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution10
        fields = ['week','email','task', 'solution']

class userssolution11Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution11
        fields = ['week','email','task', 'solution']

class userssolution12Form(forms.ModelForm):
    week = forms.ChoiceField(choices=[('week1','week1'),('week2','week2'),('week3','week3'),('week4','week4'),('week5','week5'),('week6','week6'),('week7','week7'),('week8','week8'),('week9','week9'),('week10','week10'),('week11','week11'),('week12','week12')])
    email = forms.CharField(widget=forms.TextInput(), required=True)
    task = forms.CharField(widget=forms.TextInput(), required=True, max_length=100,)
    solution = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)

    class Meta:
        model = userssolution12
        fields = ['week','email','task', 'solution']






