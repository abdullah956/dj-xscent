from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def product_view(request):
    return render(request, 'product.html')

def contact_view(request):
    return render(request, 'contact.html')

def allproducts_view(request):
    return render(request, 'all_products.html')

def blogs_view(request):
    return render(request, 'blog.html')

def thanks_view(request):
    return render(request, 'thanks.html')