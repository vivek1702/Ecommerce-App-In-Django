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
    if request.GET.get('product_sku'):
        product = VendorProducts.objects.get(product__product_sku = request.GET.get('product_sku'))
    
    product_variants = []
    if product.product.product_variants.exists():
        parent_variants = product.product.product_variants.prefetch_related('variant_option')
        for variant in parent_variants:
            product_variants.extend(
                {
                    "product_sku": product.product.product_sku,
                    "option_name": option.option_name,
                    "variant_name": option.variant_name
                }
                for option in variant.variant_option.all()
            )

    
    variant_products = []
    if product.product.parent_product:
        variant_products = [product.product.parent_product]
    else:
        variant_products = product.product.variants_products.all()
    
    for vp in variant_products:
        product_variant = ProductVariant.objects.filter(product=vp).first()
        product_variants.extend(
            {
                "product_sku": vp.product_sku,
                "option_name": option.option_name,
                "variant_name": option.variant_name
            }
            for option in product_variant.variant_option.all()
        )

    result = {}
    sorted_variants = sorted(product_variants, key=lambda x:x['product_sku'])
    for variant in sorted_variants:
        product_sku = variant['product_sku']
        variant_string = f"{variant['variant_name']}: {variant['option_name']}"
        
        if product_sku in result:
            result[product_sku].add(variant_string)  
        else:

            result[product_sku] = {variant_string}

    for product_sku in result:
        result[product_sku] = " ".join(result[product_sku])

    context = {
        'product': product,
        'product_variants': result,
    }

    print(result)

    return render(request, 'home/product_details.html', context)


