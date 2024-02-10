from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']

class loginform(forms.Form):
    email=forms.CharField()
    password=forms.CharField()