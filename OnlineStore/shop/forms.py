from cProfile import label, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        required=False
    )
    address1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address1'}),
        required=False
    )
    address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address2'}),
        required=False
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
        required=False
    )
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}),
        required=False
    )
    zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}),
        required=False
    )
    country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Password'})
    )

    new_password2 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'retype Password'})
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        required=False)

    last_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        required=False)

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        required=False)

    user_name = forms.CharField(
        label="", max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
        required=False)

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
            'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'retype Password'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'user_name', 'password1', 'password2')
