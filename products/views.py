from django.shortcuts import render

def product_view(request):
    return render(request, 'products/product.html')

def allproducts_view(request):
    return render(request, 'products/all_products.html')