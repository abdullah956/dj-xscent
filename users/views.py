from django.shortcuts import render,redirect
from .models import ContactMessage
from .models import Blog
from django.contrib import messages
from products.models import Product, Category
from .forms import NewsletterForm
from django.http import HttpResponse

def home_view(request):
    new_arrivals = Product.objects.filter(is_new_arrival=True)
    best_selling = Product.objects.filter(is_best_selling=True)
    blogs = Blog.objects.order_by('-created_at')[:3]
    categories = Category.objects.all()

    return render(request, 'home.html', {
        'new_arrivals': new_arrivals,
        'best_selling': best_selling,
        'blogs': blogs,
        'categories': categories,
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
    return render(request, 'home.html')

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Invalid email. Please try again.")
    return redirect(request.META.get('HTTP_REFERER', '/'))