from django.db       import models

class TimeStampModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Order(TimeStampModel):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    cart       = models.ForeignKey('carts.Cart', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class OrderItem(TimeStampModel):
    order      = models.ForeignKey('Order', on_delete=models.CASCADE)
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity   = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'order_items'


