from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-group'}))
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ["username","last_name","email","password1","password2"]