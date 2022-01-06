from django.urls import path 

from products.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<str:serial_number>', ProductDetailView.as_view()),
]