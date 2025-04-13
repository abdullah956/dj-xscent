from django.shortcuts import render
from .models import Blog


def home_view(request):
    return render(request, 'home.html')

def blogs_view(request):
    blogs = Blog.objects.order_by('created_at')
    return render(request, 'users/blog.html', {'blogs': blogs})

def contact_view(request):
    return render(request, 'users/contact.html')