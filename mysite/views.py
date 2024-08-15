from django.shortcuts import render,HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse

from .bot import send_message
from django.contrib import messages
from .models import Contact, Testimonial,About,Product

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]              
            phone_numer = form.cleaned_data["phone_numer"]  # Corrected this line
            description = form.cleaned_data["description"]
        

            send_message(name,email ,phone_numer , description )

            form = ContactForm()  # Reset the form after successful submission
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...')
            return HttpResponseRedirect(reverse('contact-pages'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def home_view(request):
    about = About.objects.all()
    products = Product.objects.order_by('-id')[:6]
    context = {
        "about": about,
        "products": products,  # O'zgaruvchining nomini "products" qilib o'zgartiring
    }
    return render(request, 'index.html', context)

def about_view(request):
    about=About.objects.all()
    context={
        "about":about,
    }
    return render(request,'about.html', context)

def product_view(request):
    product=Product.objects.all()
    context={
        "product":product,
    }
    return render(request,'product.html',context=context)



def testimonial_views(request):
    testimonial=Testimonial.objects.all()
    context={
        "testimonial":testimonial,
    }
    return render(request,'testimonial.html' , context)
