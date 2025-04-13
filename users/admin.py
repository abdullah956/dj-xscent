from django.contrib import admin
from users.models import Blog , ContactMessage , NewsletterSubscriber


admin.site.register(Blog)

admin.site.register(ContactMessage)

admin.site.register(NewsletterSubscriber)