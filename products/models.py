from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name     = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategories'

class Product(models.Model):
    name          = models.CharField(max_length=30)
    subcategory   = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=30)
    price         = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock         = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product

class Image(models.Model):
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)
    main_image   = models.URLField(max_length=2000) 
    detail_image = models.URLField(max_length=2000)

    class Meta:
        db_table = 'images'

class Storage(models.Model):
    storage = models.CharField(max_length=10, default=256)

    class Meta:
        db_table = 'storages'

class Product_Storage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
