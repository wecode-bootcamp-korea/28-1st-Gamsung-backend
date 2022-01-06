from django.urls import path
from carts.views import CartView

app_name = "carts"

urlpatterns = [
    path('', CartView.as_view()),
    path('/<int:id>', CartView.as_view(), name="cart-delete"),
]
