from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))