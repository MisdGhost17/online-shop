from django.shortcuts import render, redirect
from cart.forms import CartAddProductForm
from products.models import Product, ProductCategory, ProductImage
from products.forms import ProductSearchForm
from cart.cart import Cart

def redirect_to_allproducts(request):
    return redirect("allproducts")

def allproducts(request):
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    context = {
        'title': 'TechShop',
        'categories': ProductCategory.objects.all(),
        'cart_product_form': cart_product_form,
        'products_in_cart': cart.len_all_products_in_cart(),
        'cat_sort': False,
    }
    if request.method == 'POST':
        form = ProductSearchForm(data=request.POST)
        if form.is_valid():
            context['products']= Product.objects.filter(name__icontains=form.cleaned_data['search_field'])
            context['search_form']= form
    else:
        form = ProductSearchForm()
        context['products'] = Product.objects.all()
        context['search_form'] = form
    return render(request, 'products/index.html', context)


def show_products_for_category(request, cat_id):
    category = ProductCategory.objects.get(pk=cat_id)
    products = Product.objects.filter(category=cat_id)
    cart_product_form = CartAddProductForm()
    context = {
        'title': category.name,
        'categories': ProductCategory.objects.all(),
        'cart_product_form': cart_product_form,
        'cat_sort': True,
        'cat_id': category.id,
    }
    if request.method == 'POST':
        form = ProductSearchForm(data=request.POST)
        if form.is_valid():
            products = products.filter(name__icontains=form.cleaned_data['search_field'])
            context['products']= products
            context['search_form'] = form
    else:
        context['products'] = products
        context['search_form'] = ProductSearchForm()
    return render(request, 'products/index.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_product_form = CartAddProductForm()
    product_images = ProductImage.objects.filter(product=product_id)
    context = {
        'cart_product_form': cart_product_form,
        'categories': ProductCategory.objects.all(),
        'title': product.name,
        'product': product,
        'product_images': product_images,
        'search_form': ProductSearchForm(),
    }
    return render(request, 'products/product_detail.html', context)