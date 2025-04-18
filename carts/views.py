from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404, redirect


def cart_view(request):
    return render(request, 'carts/cart.html')

def checkout_view(request):
    return render(request, 'carts/checkout.html')

def thanks_view(request):
    return render(request, 'carts/thanks.html')


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'name': product.name,
            'price': float(product.price),
            'image': product.image.url,
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart

    return redirect('cart')