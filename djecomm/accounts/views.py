from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from home.models import *
from django.db.models import Sum, Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(email=email)

        if user_obj.exists():
            messages.error(request, "email already exists !")
            return redirect("/accounts/register/")
        else:
            user_obj = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = phone_number,
                email = email
            )
            user_obj.set_password(password)
            user_obj.save()
            
            messages.error(request, "Account Created: Successfully")
            return redirect("/accounts/register/")


    return render(request, "registration.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('phone_number')
        password = request.POST.get('password')
        user_obj = User.objects.filter(
          username = username
            )
        if not user_obj.exists():
            messages.debug(request, "1")
            messages.error(request, 'Error: Username does not exist')
            return redirect('/')

       
        user_obj = authenticate(username = username , password = password)

        if not user_obj:
            messages.error(request, 'Error: Invalid credentials')
            return redirect('/')
        
        login(request, user_obj)
        return redirect('/')
        

    return redirect(request , '/')


def logout_view(request):
    logout(request)
    messages.error(request, 'Success:Logged successfull')
    return redirect("/")
