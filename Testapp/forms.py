from Testapp.models import Student
from django import forms
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'



class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
