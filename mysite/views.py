from django.shortcuts import render

def home_view(request):
    return render(request=request,template_name='index.html')

def about_view(request):
    return render(request=request,template_name='about.html')

def contact_views(request):
    return render(request=request,template_name='contact.html')

def product_view(request):
    return render(request=request,template_name='product.html')

def testimonial_views(request):
    return render(request=request,template_name='testimonial.html')
