from django.urls import path
from .views import orders_list, update_order_status

urlpatterns = [
    path('orders/', orders_list, name='orders_list'),
    path('orders/update/<int:order_id>/', update_order_status, name='update_order_status'),
]
