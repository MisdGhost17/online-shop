from django.shortcuts import render
from cart.forms import CartAddProductForm
from products.models import Product, ProductCategory
from products.forms import ProductSearchForm
from django.core.paginator import Paginator

def allproducts(request):

    page = request.GET.get("page", 1)
    paginator = Paginator(Product.objects.all(), 10)
    current_page = paginator.page(int(page))

    cart_product_form = CartAddProductForm()
    context = {
        'title': 'Shop',
        'categories': ProductCategory.objects.all(),
        'cart_product_form': cart_product_form,
        'cat_sort': False,
    }
    if request.method == 'POST':
        form = ProductSearchForm(data=request.POST)
        if form.is_valid():
            paginator = Paginator(Product.objects.filter(name__icontains=form.cleaned_data['search_field']), 2)
            current_page = paginator.page(int(page))
            context['products']= current_page
            context['search_form']= form
    else:
        form = ProductSearchForm()
        context['products'] = current_page
        context['search_form'] = form
    return render(request, 'products/index.html', context)


def show_products_for_category(request, cat_id):
    category = ProductCategory.objects.get(pk=cat_id)
    products = Product.objects.filter(category=cat_id)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))
    context = {
        'title': category.name,
        'categories': ProductCategory.objects.all(),
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
        context['products'] = current_page
        context['search_form'] = ProductSearchForm()
    return render(request, 'products/index.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'title': product.name,
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)