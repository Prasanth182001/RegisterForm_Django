from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from signup.forms import myform
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created !')
            return redirect('LOGIN')
        else:
            messages.warning(request,'Password Mismatching..!!')
            return redirect('REGISTER')
    else:
        form = myform(request.POST)
        return render(request,'signup.html',{'form':form})

def profile(request):
    return render(request,'profile.html')
