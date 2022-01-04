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
                "id"         : cart.id,
                "product_id" : cart.product.id,
                "price"      : cart.product.price,
                "quantity"   : cart.quantity,
                "detail_url" : cart.product.detail_url,
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
        cart.quantity += quantity
        cart.save()
        return JsonResponse({"message" : "SUCCESS"}, status=200)
