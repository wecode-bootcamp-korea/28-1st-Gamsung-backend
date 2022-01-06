import json
from django.shortcuts       import render

from django.http            import JsonResponse
from django.views           import View

from .models                import Cart
from products.models        import Product
from utils.login_required   import login_required
from utils.validator        import validate_cart_quantity


class CartView(View):
    @login_required
    def get(self, request):
        user      = request.user
        carts     = Cart.objects.select_related('product').filter(user_id = user.id)

        cart_list = [{
                "id"            : cart.id,
                "product_id"    : cart.product.id,
                "product_name"  : cart.product.name,
                "serial_number" : cart.product.serial_number,
                "price"         : cart.product.price,
                "quantity"      : cart.quantity,
                "main_url"      : Product.objects.get(name=cart.product).mainimage_set.first().main_url,
            }for cart in carts]
            
        return JsonResponse({"cart_list" : cart_list}, status=200)

    @login_required
    def post(self, request):
        data       = json.loads(request.body)
        user       = request.user
        product_id = data['product_id']
        quantity   = int(data['quantity'])

        cart, created  = Cart.objects.get_or_create(
            user_id    = user.id,
            product_id = product_id
        )
        
        if not validate_cart_quantity(quantity):
            return JsonResponse({"message" : "Bad Request"}, status=400)
        
        if created:
            cart.quantity = quantity
        else:
            cart.quantity += quantity
        
        cart.save()

        return JsonResponse({"message" : "SUCCESS"}, status=200)

    @login_required
    def patch(self, request):
        try:
            data     = json.loads(request.body)
            user     = request.user
            product_id  = int(data['product_id'])
            quantity = int(data['quantity'])

            cart = Cart.objects.filter(user_id=user.id, product_id=product_id).get()

            if quantity == 1:  
                cart.quantity += 1

            if quantity == -1:
                if cart.quantity <= 1:
                    cart.quantity == 1
                else:
                    cart.quantity -= 1

            cart.save()
            return JsonResponse({"message" : "SUCCESS"}, status=200)
            
        except Cart.DoesNotExist:
            return JsonResponse({"message" : "INVALID_CART"}, status=400)

    @login_required
    def delete(self, request, id):
        try:
            user    = request.user

            cart = Cart.objects.get(user_id=user.id, product_id=id)
            cart.delete()

            return JsonResponse({"message" : "DELETED"}, status=204)

        except Cart.DoesNotExist:
            JsonResponse({"message" : "Cart Does Not Exist"}, status=404)
