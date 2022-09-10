from django.contrib import admin
from ki.models import Product, Category, Order, Profile
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
