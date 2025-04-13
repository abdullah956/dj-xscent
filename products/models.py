from django.db import models
from config.models import BasedModel


class Category(BasedModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
 
class Product(BasedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_best_selling = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name