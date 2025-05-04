from django.db import models
from config.models import BasedModel

class Orders(BasedModel):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD_CHOICES,
        default='cod',
    )
    cart_data = models.JSONField(default=dict)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.payment_method}'
