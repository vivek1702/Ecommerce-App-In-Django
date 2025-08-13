import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'djecomm.settings'
django.setup()


from products.models import *
import pandas as pd
from django.db import transaction
import random

Volume_choices = ['500ml', '250ml', '1l', '2l', '100ml']
color_choices = ['red', 'blue', 'green', 'yellow']
weight_choice = ['500g', '1kg', '2kg']


def generating_random_options(variant):
    if variant == "Volume":
        return random.choice(Volume_choices)
    elif variant == "Colour":
        return random.choice(color_choices)
    elif variant == "Display weight":
        return random.choice(weight_choice)
    else:
        return f"{variant}--{random.randint(1,100)}"
 
def upload_products_from_excel(path_file):
    try:
        df = pd.read_excel(path_file)
        with transaction.atomic():
            for index, row in df.iterrows():
                category, _ = Category.objects.get_or_create(name = row['Material category'])
                subCategory, _ = SubCategory.objects.get_or_create(
                    category = category,
                    name = row['Sub category level 1']
                )

                brand, _ = brandName.objects.get_or_create(name = row['Brand name'])

                if row['Variation type'] in ['Parent only', 'Parent with variant/s']:
                    parent_product = Products.objects.create(
                        category = category,
                        sub_category = subCategory,
                        brand_name = brand,
                        item_name = row['Item name title'],
                        product_description = row['Product description'],
                        product_sku = row['Product SKU'],
                        hsn_code = row['HSN code'],
                        maximum_retail_price = random.randint(1000, 999999)
                    )

                    if row['Variation type'] == 'Parent with variant/s':
                        variant_theme = row['Variation_theme']
                        variants = variant_theme.split("+")
                        for variant in variants:
                            option_name = generating_random_options(variant)
                            variant_option, _ = VariantsOptions.objects.get_or_create(
                                variant_name = variant,
                                variant_option = option_name
                            )

                if row['Variation type'] == 'Variant':
                    parent_product = Products.objects.get(product_sku = row['Parent SKU'])
                    variant_options = []
                    parent_variant_options = []

                    variant_theme = row['Variation_theme']
                    variants = variant_theme.split("+")
                    for variant in variants:
                        option_name = generating_random_options(variant)
                        variant_option, _ = VariantsOptions.objects.get_or_create(
                            variant_name = variant,
                            variant_option = option_name
                        )
                        variant_options.append(variant_option)

                    for variant in variants:
                        option_name = generating_random_options(variant)
                        variant_option, _ = VariantsOptions.objects.get_or_create(
                            variant_name = variant,
                            variant_option = option_name
                        )
                        parent_variant_options.append(variant_option)

                    variant_product = Products.objects.create(
                        category = category,
                        sub_category = subCategory,
                        brand_name = brand,
                        item_name = row['Item name title'],
                        product_description = row['Product description'],
                        product_sku = row['Product SKU'],
                        hsn_code = row['HSN code'],
                        parent_product = parent_product,
                        maximum_retail_price = random.randint(1000, 999999)
                    )

                    parent_product_variant = ProductVariant.objects.create(product = parent_product)
                    parent_product_variant.variant_option.add(*parent_variant_options)
                    product_variant = ProductVariant.objects.create(product = variant_product)
                    product_variant.variant_option.add(*variant_options)


    except Exception as e:
        print(e)              

# upload_products_from_excel('C:\\Users\\svive\\Ecommerce Web App\\djecomm\\PRODUCTS.xlsx')



from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def list_files(start_path):
    all_files = []
    for root, dirs, files in os.walk(start_path):
        all_files.extend(
            {"path": os.path.join(root, filename), "file":filename}

            for filename in files
        )

    return all_files


def getProductFromImageName(imageName):
    try:
        imgaeName = imageName.split('.')[0]
        return True, Products.objects.get(product_sku= imageName), imageName
    except Exception as e:
        pass
    return False, "", "imageName"


def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True 
    except Exception as e:
        return False
    
def uploadImages(path):

    dir_path = f"{path}"
    file_lists = list_files(dir_path)

    for file_list in file_lists:
        try:
            filename = file_list['file']
            path = file_list['path']
            filename_without_extension = os.path.splitext(filename)[0]
            status, sku, image_name = getProductFromImageName(filename_without_extension)
            print(status)
            if status:
                with open(path, 'rb') as file:
                    upload_file = SimpleUploadedFile(path, file.read())
                    ProductImage.objects.create(
                        product = sku,
                        image = upload_file
                    )
            
        except Exception as e:
            print(e)


# uploadImages('C:\\Users\\svive\\Ecommerce Web App\\djecomm\\images\\Birla Shakti Images')


#creating vendor products
def vendor_product_create():
    shopkeeper_1 = Shopkeeper.objects.first()
    for product_c in Products.objects.all():
        price = random.randint(100, 1000)
        if VendorProducts.objects.filter(product=product_c, shopkeeper=shopkeeper_1):
            continue
        VendorProducts.objects.create(
        shopkeeper = shopkeeper_1,
        product = product_c,
        vendor_selling_price = price,
        dealer_price = price - random.randint(10,100),
        )


vendor_product_create()

    
        



