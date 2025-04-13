from django.urls import path
from .views import home_view,cart_view,checkout_view,product_view,contact_view,allproducts_view,blogs_view,thanks_view

urlpatterns = [
    path('', home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('product/', product_view, name='product'),
    path('contact/', contact_view, name='contact'),
    path('all/', allproducts_view, name='all_products'),
    path('blogs/', blogs_view, name='blog'),
    path('orderplaced/', thanks_view, name='thanks'),

]
