from django.urls import path
from .views import cart_view,add_to_cart,remove_from_cart,update_cart_quantity

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart-quantity/', update_cart_quantity, name='update_cart_quantity'),

]
