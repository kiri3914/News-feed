from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'username', 'password1', 'password2']


class CustomUserLoginForm(AuthenticationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
