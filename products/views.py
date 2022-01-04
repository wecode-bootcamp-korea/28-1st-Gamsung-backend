import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from users.models    import User
from products.models import SubCategory, Product, MainImage, DetailImage, Storage, ProductStorage

class ListView(View): 
    def get(self, request):
        sort_by = {
            'id'         : 'id',
            'high_price' : '-price',
            'low_price'  : 'price',
            'new'        : '-created_at',
            'old'        : 'created_at'               
        }

        order_condition = request.GET.get('order_condition', None)
        filter_options  = request.GET.getlist('filter_options', None)
        offset          = int(request.GET.get('offset', 0))
        limit           = offset + int(request.GET.get('limit', 10))

        product_condition = Q()
        if filter_options:
            product_condition &= Q(subcategory__in = filter_options)
        products = Product.objects.filter(product_condition).order_by(sort_by.get(order_condition, 'id'))[offset:limit]

        products_list = [{
                'name'         : product.name, 
                'subcategory'  : SubCategory.objects.get(product=product).name, 
                'serial_number': product.serial_number, 
                'storage'      : ProductStorage.objects.get(product=product).storage.storage, 
                'price'        : product.price, 
                'main_image'   : MainImage.objects.get(product=product).main_url, 
                'detail_images': [detail_image.detail_url for detail_image in DetailImage.objects.filter(product=product)]
                } for product in products]
        return JsonResponse({'results':products_list}, status=200)

class DetailView(View):
    def get(self, request, serial_number):
        product              = Product.objects.get(serial_number=serial_number)
        product_details_list = [{
                'name'         : product.name, 
                'serial_number': product.serial_number, 
                'storage'      : ProductStorage.objects.get(product=product).storage.storage, 
                'price'        : product.price, 
                'main_image'   : MainImage.objects.get(product=product).main_url, 
                'detail_images': [detail_image.detail_url for detail_image in DetailImage.objects.filter(product=product)]
                }]
        return JsonResponse({"results": product_details_list}, status=200)
