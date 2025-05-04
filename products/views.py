from .models import Product, Category , Review
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = Review.objects.filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    avg_rating = round(avg_rating)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = int(request.POST.get('rating'))
        review_message = request.POST.get('review')

        Review.objects.create(
            product=product,
            name=name,
            email=email,
            rating=rating,
            review=review_message
        )
        return redirect('product', id=product.id)

    return render(request, 'products/product.html', {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'stars': range(1, 6),
    })

def allproducts_view(request):
    category_id = request.GET.get('category')
    price_filter = request.GET.get('price')
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if price_filter == 'below1500':
        products = products.filter(price__lt=1500)
    elif price_filter == '1500to2500':
        products = products.filter(price__gte=1500, price__lte=2500)
    elif price_filter == 'above2500':
        products = products.filter(price__gt=2500)

    categories = Category.objects.all()
    return render(request, 'products/all_products.html', {
        'products': products,
        'categories': categories,
    })
