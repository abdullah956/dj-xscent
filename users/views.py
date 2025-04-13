from django.shortcuts import render,redirect
from .models import ContactMessage
from .models import Blog
from django.contrib import messages
from products.models import Product

def home_view(request):
    new_arrivals = Product.objects.filter(is_new_arrival=True)
    best_selling = Product.objects.filter(is_best_selling=True)
    blogs = Blog.objects.order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'new_arrivals': new_arrivals,
        'best_selling': best_selling,
        'blogs': blogs,
    })

def blogs_view(request):
    blogs = Blog.objects.order_by('created_at')
    return render(request, 'users/blog.html', {'blogs': blogs})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'users/contact.html')
