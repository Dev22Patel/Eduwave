from django.urls import path
from .views import add_cart,cart,delete_item # Make sure this import matches your view function


urlpatterns = [
    path('add_cart/<c_uid>/',add_cart,name="add_cart"),
    path('cart/',cart,name='cart'),
    path('delete/<cart_item_uid>',delete_item,name='delete_item'),
]
