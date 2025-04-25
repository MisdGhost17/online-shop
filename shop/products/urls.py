from django.shortcuts import redirect
from django.urls import path
from products.views import allproducts, show_products_for_category, product_detail, redirect_to_allproducts
from cart.views import add_product, remove_product, cart_detail, update_product


urlpatterns = [
    path('search/', allproducts, name='searchproducts'),
    path('search_in_cat/<int:cat_id>/', show_products_for_category , name='search_products_in_category'),
    path('product=<int:product_id>/', product_detail, name='productdetail'),
    path('addproduct/<int:product_id>/', add_product, name='addproduct'),
    path('removeproduct/<int:product_id>/', remove_product, name='removeproduct'),
    path('updateproduct/<int:product_id>/', update_product, name='updateproduct'),
    path('cart/', cart_detail, name='cart'),
    path('allproduct', allproducts, name='allproducts'),
    path('', redirect_to_allproducts, name='redirect_allproducts'),
    path('category/<int:cat_id>/', show_products_for_category ,name='showcategoryproducts'),
]
