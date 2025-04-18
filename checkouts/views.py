from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Orders
from decimal import Decimal


def checkout_view(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        total = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())

        order = Orders.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            street_address=request.POST.get('street_address'),
            city=request.POST.get('city'),
            postal_code=request.POST.get('postal_code'),
            payment_method=request.POST.get('paymentMethod'),
            cart_data=cart,
            total_amount=total,
            paid=False
        )

        item_lines = []
        for item in cart.values():
            name = item['name']
            quantity = item['quantity']
            price = item['price']
            total_price = round(Decimal(price) * quantity, 2)
            item_lines.append(f'{name} x {quantity} = Rs. {total_price:.2f}')
        message = 'Thank you for your order!\n\nHere is your order summary:\n\n'
        message += '\n'.join(item_lines)
        message += f'\n\nGrand Total: Rs. {total:.2f}\n\nWe appreciate your business.'
        subject = 'Your Order Confirmation'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [order.email],
            fail_silently=False
        )
        request.session['cart'] = {}
        request.session['cart_total'] = 0
        return redirect('thanks')

    return render(request, 'checkouts/checkout.html')


def thanks_view(request):
    return render(request, 'checkouts/thanks.html')