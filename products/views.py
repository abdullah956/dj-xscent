from django.shortcuts import render
from .models import Product, Category


def product_view(request):
    return render(request, 'products/product.html')


def allproducts_view(request):
    category_id = request.GET.get('category')
    price_filter = request.GET.get('price')
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if price_filter == 'below1500':
        products = products.filter(price__lt=1500)
    elif price_filter == '1500to2500':
        products = products.filter(price__gte=1500, price__lte=2500)
    elif price_filter == 'above2500':
        products = products.filter(price__gt=2500)

    categories = Category.objects.all()
    return render(request, 'products/all_products.html', {
        'products': products,
        'categories': categories,
    })
