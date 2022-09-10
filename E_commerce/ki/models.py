from django.db import models
from account.models import MyUser
from phonenumber_field.modelfields import PhoneNumberField

    
class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    phone_number = PhoneNumberField(blank=True, verbose_name="Phone number(+234.....)")
    date_of_birth = models.DateField(blank=True)
    user_image = models.ImageField(upload_to="user_image", blank=True)

    def __str__(self):
        return self.user

class Category(models.Model):
    category = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
    images = models.ImageField(upload_to="product_images")

    def __str__ (self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.products.name