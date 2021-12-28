from django.db       import models

from users.models    import User
from products.models import Product, Storage

class Cart(models.Model):
    user       = models.ForeignKey('User', on_delete=models.CASCADE)
    product    = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField(default=1)
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carts'
    
    def sub_total(self):
        return self.product.price * self.quantity