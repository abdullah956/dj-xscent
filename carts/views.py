from django.shortcuts import render
from products.models import Product
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_total = 0
    for item in cart.values():
        item['item_total'] = float(item['price']) * item['quantity']
        cart_total += item['item_total']
    request.session['cart_total'] = cart_total

    return render(request, 'carts/cart.html', {'cart': cart})


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

    total = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())
    request.session['cart'] = cart
    request.session['cart_total'] = float(total)

    return redirect('cart')

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart

    return redirect('cart')

@csrf_exempt
def update_cart_quantity(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        product_id = request.POST.get('id')
        quantity = int(request.POST.get('quantity'))

        if product_id in cart:
            cart[product_id]['quantity'] = quantity
            request.session['cart'] = cart

            item_total = float(cart[product_id]['price']) * quantity
            total = sum(float(item['price']) * item['quantity'] for item in cart.values())
            request.session['cart_total'] = total

            return JsonResponse({
                'success': True,
                'item_total': f'{item_total:.2f}',
                'total_price': f'{total:.2f}'
            })

    return JsonResponse({'success': False})