from django.db import models
from utils.models import BaseModel
from accounts.models import Shopkeeper

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=200)
    comission_percentage = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class brandName(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Products(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="product_sub_category")
    brand_name = models.ForeignKey(brandName, on_delete=models.CASCADE, related_name="product_brand")
    item_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_sku = models.CharField(max_length=1000, unique=True)
    hsn_code = models.CharField(max_length=1000, null=True, blank=True)
    parent_product = models.ForeignKey("Products", on_delete=models.CASCADE, related_name="variants_products", null=True, blank=True)
    maximum_retail_price = models.FloatField()

    def __str__(self):
        return self.item_name
    
    def getFirstImage(self):
        if self.product_image.first():
            return  self.product_image.first().image

        return "https://static.vecteezy.com/system/resources/thumbnails/022/014/063/small/missing-picture-page-for-website-design-or-mobile-app-design-no-image-available-icon-vector.jpg"
    

    
class VariantsOptions(BaseModel):
    variant_name = models.CharField(max_length=200)
    variant_option = models.CharField(max_length=200)

    def __str__(self):
        return self.variant_option
    


class ProductVariant(BaseModel):
    product = models.ForeignKey(Products, related_name="product_variants", on_delete=models.CASCADE)
    variant_option = models.ManyToManyField(VariantsOptions)

    def __str__(self):
        return f"product variant {self.product.item_name}"
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Products, related_name="product_image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/",null=True)



class VendorProducts(BaseModel):
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    vendor_selling_price = models.FloatField()
    dealer_price = models.FloatField()
    is_active = models.BooleanField(default=True)
    delivery_fee = models.FloatField(default=0)

    def get_product_details(self):
        return {
            "product_name": self.product.item_name,
            "product_image": self.product.getFirstImage()
        }



