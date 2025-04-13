from django.shortcuts import render

def cart_view(request):
    return render(request, 'carts/cart.html')

def checkout_view(request):
    return render(request, 'carts/checkout.html')

def thanks_view(request):
    return render(request, 'carts/thanks.html')