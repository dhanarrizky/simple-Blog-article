from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrasionForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",  "placeholder":"Email Address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" , "placeholder":"User Name"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" , "placeholder":"Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password (Again)"}))
    
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')