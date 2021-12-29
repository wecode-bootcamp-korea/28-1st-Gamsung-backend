from django.db       import models

from core.models import TimeStampModel

class Cart(TimeStampModel):
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product   = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity  = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'carts'
    
    def sub_total(self):
        return self.product.price * self.quantity
