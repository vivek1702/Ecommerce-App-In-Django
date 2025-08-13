from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from home.models import *
from django.db.models import Sum, Q
from django.contrib.auth.decorators import login_required
from products.models import *

# Create your views here.

def home(request):
    category = Category.objects.all()
    product = VendorProducts.objects.all()[:30]
    context = {
        "categories" : category,
        "products" : product
    }
    return render(request, "home/home.html", context)

def product_details(request, id):
    product = VendorProducts.objects.get(id=id)
    print(VendorProducts.product.variants_products.all())
    context = {"product":product}
    return render(request, "home/product_details.html", context)
