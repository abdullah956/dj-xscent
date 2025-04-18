from django.urls import path
from .views import product_view,allproducts_view

urlpatterns = [
    path('product/<int:id>/', product_view, name='product'),
    path('all_products/', allproducts_view, name='all_products'),
]
