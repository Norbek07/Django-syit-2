from django.contrib import admin
from .models import Contact,Testimonial,About,Product

# Register your models here.

admin.site.register((Contact,Product))


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','img',"description","job")

@admin.register(About)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('img1',"img2",)
