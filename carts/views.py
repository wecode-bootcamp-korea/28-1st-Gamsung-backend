import json
from django.shortcuts       import render

from django.http            import JsonResponse
from django.views           import View

from .models                import Cart
from utils.login_required   import login_required

class CartView(View):
    @login_required
    def get(self, request):
        user      = request.user
        carts     = Cart.objects.select_related('user__product').filter(user_id = user.id)
        cart_list = [{
                "id"            : cart.id,
                "product_id"    : cart.product.id,
                "product_name"  : cart.product.name,
                "serial_number" : cart.product.serial_number,
                "price"         : cart.product.price,
                "storage"       : cart.product.storage,
                "quantity"      : cart.quantity,
                "main_url"      : cart.product.main_url,
            }for cart in carts]

        return JsonResponse({"cart_list" : cart_list}, status=200)

    @login_required
    def post(self, request):
        data       = json.loads(request.body)
        user       = request.user
        product_id = data['product_id']
        quantity   = data['quantity']

        cart, created  = Cart.objects.get_or_create(
            user_id    = user.id,
            product_id = product_id
        )

        if created:            
            cart.quantity = quantity
        else:
            cart.quantity += quantity
        
        cart.save()

        return JsonResponse({"message" : "SUCCESS"}, status=200)

    @login_required
    def patch(self, request):
        data     = json.loads(request.body)
        user     = request.user
        cart_id  = data['cart_id']
        quantity = int(data['quantity'])

        cart = Cart.objects.filter(user_id=user.id, cart_id=cart_id).get()
    
        if quantity == 1:      
            cart.quantity += 1
        if quantity == -1:
            cart.quantity -= 1
            if cart.quantity < 1:
                pass
        cart.save()

    @login_required
    def delete(self, request):
        try:
            user = request.user
            cart_id = request.GET.get('id')

            cart = Cart.objects.get(user_id=user.id, id=cart_id)
            cart.delete()

            return JsonResponse({"message" : "DELETED"}, status=200)

        except KeyError:
            JsonResponse({"message" : "KEY ERROR"}, status=400)
