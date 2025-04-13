from django.urls import path
from .views import home_view,contact_view,blogs_view,newsletter_signup

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('blog/', blogs_view, name='blog'),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
]
