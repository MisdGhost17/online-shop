from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

from .cart import Cart
from .forms import CartAddProductForm

@login_required(login_url='login')
def add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = CartAddProductForm(data=request.POST)
    if form.is_valid():
        cart.add(product,
                 quantity=form.cleaned_data['quantity'],
                 override_quantity=form.cleaned_data['override'])
    return redirect('allproducts')

@login_required(login_url='login')
def remove_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart')

@login_required(login_url='login')
def update_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = CartAddProductForm(data=request.POST)
    if form.is_valid():
        cart.add(product,
                 quantity=form.cleaned_data['quantity'],
                 override_quantity=form.cleaned_data['override'])
    return redirect('cart')

@login_required(login_url='login')
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    context = {
        'products_in_cart': cart.len_all_products_in_cart(),
        'cart': Cart(request),
    }
    return render(request, 'cart/cart_detail.html', context)
