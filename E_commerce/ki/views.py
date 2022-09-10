from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def aboutus(request):
    return render(request, "aboutus.html", {})

def test(request):
    return render(request, "text.html")

def index(request):
    return render(request, "index.html", {})

@login_required(login_url='authentication_login')
def account_dashboard(request):
    return render(request, "account_dashboard.html", {})

def account_edit(request):
    return render(request, "account_edit_profile.html", {})

# def account_orders(request):
    # return render(request, "account_orders.html", {})

def account_profile(request):
    return render(request, "account_profile.html", {})

def address(request):
    return render(request, "address.html", {})

def billing_details(request):
    return render(request, "billing_details.html", {})

def blog_post(request):
    return render(request, "blog_post.html", {})

def blog_read(request):
    return render(request, "blog_read.html", {})

def cart(request):
    return render(request, "cart.html", {})

def contact_us(request):
    return render(request, "contact_us.html", {})

def payment_method(request):
    return render(request, "payment_method.html", {})

def product_details(request):
    return render(request, "product_details.html", {})

def search(request):
    return render(request, "search.html", {})

def shop_grid(request):
    return render(request, "shop_grid.html", {})

def shop_grid_type_4(request):
    return render(request, "shop_grid_type_4.html", {})

def shop_grid_type_5(request):
    return render(request, "shop_grid_type_5.html", {})

def thank_you(request):
    return render(request, "thank_you.html", {})

def wishlist(request):
    return render(request, "wishlist.html", {})


