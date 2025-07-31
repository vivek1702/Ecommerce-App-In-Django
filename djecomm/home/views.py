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

def home(request):
    return render(request, "home/home.html")

