from django.db import models
from config.models import BasedModel


class Blog(BasedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class ContactMessage(BasedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

class NewsletterSubscriber(BasedModel):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
