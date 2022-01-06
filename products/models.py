from django.db   import models

from core.models import TimeStampModel

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name     = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'subcategories'

class Product(TimeStampModel):
    name          = models.CharField(max_length=30)
    subcategory   = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    serial_number = models.CharField(max_length=30,unique=True)
    price         = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    stock         = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
    
class ProductStorage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    storage = models.ForeignKey('Storage', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'products_storages'

class Storage(models.Model):
    type    = models.CharField(max_length=10, default=256)
    product = models.ManyToManyField(Product, related_name='storage', through=ProductStorage)

    class Meta:
        db_table = 'storages'

class MainImage(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    main_url   = models.URLField(max_length=2000) 

    class Meta:
        db_table = 'main_images'

class DetailImage(models.Model):
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    detail_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'detail_images'