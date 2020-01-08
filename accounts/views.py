from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import myuser
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')
    
def register(request):
    if request.method=="GET":
        return render(request, 'register.html')
    elif request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if password == password2:
            myuser.objects.create_user(username=username,email= email, password=password, name=name, age=age)
            return redirect('home')
        else:
            return render(request, 'register.html')
