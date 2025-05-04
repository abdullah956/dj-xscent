from django.db import models
from config.models import BasedModel


class Category(BasedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
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

class Review(BasedModel):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # To store the name of the reviewer
    email = models.EmailField()
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    review = models.TextField()

    def __str__(self):
        return f"Review for {self.product.name} by {self.name}"