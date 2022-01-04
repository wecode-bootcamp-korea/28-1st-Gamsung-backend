import json

from django.http     import JsonResponse
from django.views    import View

from users.models    import User
from products.models import SubCategory, Product, MainImage, DetailImage, Storage, ProductStorage

class ListView(View): 
    def get(self, request):
        products = Product.objects.all()
        products_list = []
        for product in products:
            subcategory         = SubCategory.objects.get(product=product)
            main_image          = MainImage.objects.get(product=product).main_url
            detail_images_query = DetailImage.objects.filter(product=product)
            storage = ProductStorage.objects.get(product=product).storage
            detail_images_list = []
            for image in detail_images_query:
                detail_images_list.append(image.detail_url)
            products_list.append({'name':product.name, 'subcategory':subcategory.name, 'serial_number':product.serial_number, 'storage':storage.storage, 'price':product.price, 'main_image':main_image, 'detail_images':detail_images_list})
        return JsonResponse({'results':products_list}, status=200)
 

class DetailView(View):
    def get(self, request, serial_number):
        product_details_list = []
        product = Product.objects.get(serial_number=serial_number)
        main_image = MainImage.objects.get(product=product).main_url
        storage = ProductStorage.objects.get(product=product).storage
        detail_images_query = DetailImage.objects.filter(product=product)
        detail_images_list = []
        for image in detail_images_query:
            detail_images_list.append(image.detail_url)
        product_details_list.append({'name':product.name, 'serial_number':product.serial_number, 'storage':storage.storage, 'price':product.price, 'main_image':main_image, 'detail_images':detail_images_list})
        return JsonResponse({"results": product_details_list}, status=200)
