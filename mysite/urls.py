from django.urls import path
from .views import home_view, about_view, contact_views,product_view,testimonial_views

urlpatterns = [
    path('',home_view,name='home-pages'),
    path('about/',about_view ,name='about-pages'),
    path('contact/',contact_views,name='contact-pages'),
    path('product/',product_view,name='product-pages'),
    path('testimonial/',testimonial_views, name='testimonial-pages')
]
 