from django.shortcuts import render, redirect
from .models import Product
from  django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignupForm



def helloworld(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products': all_products})

def about(request):
    return render(request, 'about.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
             messages.error(request, 'Please enter correct username and password.')
             return redirect('login')
    else:
       return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def signup_user(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user= authenticate(request, username=username, password= password)
            login(request, user)
            messages.success(request, 'You are now registered')
            return redirect('home')

        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('signup_user')
    else:
        return render(request, 'signup.html', {'form': form})

