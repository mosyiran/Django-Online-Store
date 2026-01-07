from cProfile import label

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))

    user_name = forms.CharField(
        label="", max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_name')




class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))

    user_name = forms.CharField(
        label="", max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))

    password1 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name':'password','type':'password','placeholder':'Password'})
    )

    password2 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'retype Password'})
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_name', 'password1', 'password2')