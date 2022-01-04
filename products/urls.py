from django.urls import path 

from products.views import ListView, DetailView

app_name = 'products'

urlpatterns = [
    path('', ListView.as_view()),
    path('/<str:serial_number>', DetailView.as_view()),
]