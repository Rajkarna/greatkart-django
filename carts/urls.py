from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name ='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name = 'add_cart'),
    path('sub_cart/<int:product_id>/', views.sub_cart, name = 'sub_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name = 'remove_cart'),
]
