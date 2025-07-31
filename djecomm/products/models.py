from django.db import models
from utils.models import BaseModel

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




