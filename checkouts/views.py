from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from decimal import Decimal


def checkout_view(request):
    if request.method == 'POST':
        cart_data = request.session.get('cart', {})
        total_amount = Decimal(request.session.get('cart_total', 0))
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        payment_method = request.POST.get('paymentMethod')
        order = Orders.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street_address=street_address,
            city=city,
            postal_code=postal_code,
            payment_method=payment_method,
            cart_data=cart_data,
            total_amount=total_amount,
        )
        request.session['cart'] = {}
        request.session['cart_total'] = 0
        return redirect('thanks')
    
    return render(request, 'checkouts/checkout.html')

def thanks_view(request):
    return render(request, 'checkouts/thanks.html')