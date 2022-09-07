from django.shortcuts import render, redirect
from ki.forms import MyUserForm
from django.contrib import messages

# Create your views here.

def signup_user(request):
    form = MyUserForm()
    if request.method == "POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "cool work")
            return redirect('signup_user')
        else:
            messages.info(request, "invalid input")
            return redirect('signup_user')
    context = {'form':form}
    return render(request, 'signup.html', context)



def aboutus(request):
    return render(request, "aboutus.html", {})


def index(request):
    return render(request, "index.html", {})


def account_dashboard(request):
    return render(request, "account_dashboard.html", {})

def account_edit(request):
    return render(request, "account_edit.html", {})

def account_orders(request):
    return render(request, "account_orders.html", {})

def account_profile(request):
    return render(request, "account_profile.html", {})

def address(request):
    return render(request, "address.html", {})

def authentication_login(request):
    return render(request, "authentication_login.html", {})

def authentication_reset_password(request):
    return render(request, "authentication_reset_password.html", {})

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

def j   
