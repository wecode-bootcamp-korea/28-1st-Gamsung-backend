from django.db       import models

class TimeStampModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Cart(TimeStampModel):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField(default=1)
    is_active  = models.BooleanField(default=True)

    class Meta:
        db_table = 'carts'
    
    def sub_total(self):
        return self.product.price * self.quantity
