from django.shortcuts import render,redirect
from .models import ContactMessage
from .models import Blog
from django.contrib import messages


def home_view(request):
    return render(request, 'home.html')

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
