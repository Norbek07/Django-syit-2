from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone_numer = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()

    def str(self):
        return self.name
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='imgs/testimonial')
    description = models.TextField()
    job = models.CharField(max_length=20)


    def str(self):
        return f"{self.name} {self.img} {self.description} {self.job}"



class About(models.Model):
    img1 = models.ImageField(upload_to='imgs/About')
    img2 = models.ImageField(upload_to='imgs1/About')

class Product(models.Model):
    image=models.ImageField(upload_to='Images/product')
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2)

