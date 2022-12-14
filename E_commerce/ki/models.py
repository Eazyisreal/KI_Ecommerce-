from django.db import models
from accs.models import MyUser
from phonenumber_field.modelfields import PhoneNumberField

    
class Profile(models.Model):
    user = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    phone_number = PhoneNumberField(blank=True, verbose_name="Phone number(+234xxxxxxxxx)")
    date_of_birth = models.DateField(blank=True, verbose_name="Date of Birth (yyyy-mm-dd)")
    user_image = models.ImageField(upload_to="user_image", blank=True, null=True)

    def __str__(self):
        return self.user.email

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Product(models.Model):
    STATUS = (
       ( 0 , "normal_product"),
       ( 1 , "wishlist"),     
    )
    STATUS2 = (
        (2, "product"),
        (3, "Add to Cart")
    )
    username = models.ManyToManyField(MyUser,  null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.IntegerField()
    images = models.ImageField(upload_to="product_images")
    status = models.IntegerField(choices=STATUS, default=0)
    status_two = models.IntegerField(choices=STATUS2, default=2)

    def __str__ (self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.products.name

class Add_cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name