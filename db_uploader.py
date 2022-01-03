import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gamsung.settings")
django.setup()

from users.models import User 
from products.models import Product, SubCategory, Category, MainImage, DetailImage, ProductStorage, Storage  

CSV_PATH_USERS = './users.csv' 
CSV_PATH_PRODUCTS = './products.csv'

with open('users.csv') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)             
    for row in data_reader:
        User.objects.create(
            email=row[0],
            password=row[1], 
            last_name=row[2], 
            first_name=row[3], 
            date_of_birth=row[4]
        )

with open('products.csv') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)             
    for row in data_reader:
        if Product.objects.filter(serial_number=row[3]).exists():
            print({"message":{"DUPLICATED_SERIAL_NUMBER"}})
        else:
            category_name = row[0]
            if Category.objects.filter(name = category_name).exists():
                pass
            else:
                Category.objects.create(name = category_name)

            subcategory_name = row[1]
            if SubCategory.objects.filter(name = subcategory_name).exists():
                pass
            else:
                SubCategory.objects.create(category=Category.objects.get(name=category_name), name = subcategory_name)

            Product.objects.create(name = row[2], subcategory = SubCategory.objects.get(name = subcategory_name), serial_number=row[3], price=row[4], stock=row[5])
            product=Product.objects.get(serial_number=row[3])
            MainImage.objects.create(product = product, main_url = row[6])
            DetailImage.objects.create(product = product, detail_url = row[7])
            DetailImage.objects.create(product = product, detail_url = row[8])
            DetailImage.objects.create(product = product, detail_url = row[9])
            DetailImage.objects.create(product = product, detail_url = row[10])
            DetailImage.objects.create(product = product, detail_url = row[11])
            ProductStorage.objects.create(product = product,storage = Storage.objects.get(storage=row[12]))

