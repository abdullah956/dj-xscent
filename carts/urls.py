from django.urls import path
from .views import cart_view,checkout_view,thanks_view,add_to_cart,remove_from_cart

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('thanks/', thanks_view, name='thanks'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),

]
