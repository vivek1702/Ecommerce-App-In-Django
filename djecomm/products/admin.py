from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(brandName)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "sub_category",
        "brand_name",
        "item_name",
        "product_description",
        "product_sku",
        "hsn_code",
        "parent_product",
        "maximum_retail_price",
    ]

    search_fields = [
        "item_name",
        "product_description",
        "product_sku",
        "hsn_code",
    ]

class ProductVariantAdmin(admin.ModelAdmin):
    search_fields = ['product__item_name',  'product__product_sku']

admin.site.register(Products,ProductAdmin)
admin.site.register(VariantsOptions)
admin.site.register(ProductVariant,ProductVariantAdmin)
admin.site.register(ProductImage)
admin.site.register(VendorProducts, ProductVariantAdmin)
    
