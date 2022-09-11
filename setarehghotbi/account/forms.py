from django import forms
from .models import  User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'گذرواژه'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'تکرار گذرواژه'}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100', 'placeholder': 'نام کاربری'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input100', 'placeholder': 'ایمیل'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']



class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'گذرواژه'}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input100', 'placeholder': 'نام کاربری'}))



class PasswordRestFrom(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'گذرواژه'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100', 'placeholder': 'تکرار گذرواژه'}))