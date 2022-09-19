from msilib import CAB
from operator import ge
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ki.forms import ProfileForm, ContactForm
from ki.models import Profile, Contact, Product, Category


# Create your views here.


def aboutus(request):
    return render(request, "aboutus.html", {})

def base(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "base.html", context)

def test(request):
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("account_profile")
    context ={"profile_form": profile_form}
    return render(request, "text.html", context)

def index(request):
    products = Product.objects.filter(category__category__contains = "featured_products")
    context = {"products":products}
    return render(request, "index.html", context)

@login_required(login_url='authentication_login')
def account_dashboard(request):
    return render(request, "account_dashboard.html", {})



def account_orders(request):
    return render(request, "account_orders.html", {})

@login_required(login_url='authentication_login')
def account_profile(request):
    profile = Profile.objects.get(user__email = request.user.email)
    context = {"profile":profile}
    return render(request, 'account_profile.html', context)

@login_required(login_url='authentication_login')
def create_profile(request):
    profile_form = ProfileForm()
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form_add = form.save(commit=False)
            form_add.user = request.user
            form_add.save()
            return redirect('account_profile')
        error = form.errors
        return render(request, "account_edit_profile.html", {"profile_form":profile_form, "error":error})
    return render(request, "account_edit_profile.html", {"profile_form":profile_form})

@login_required(login_url='authentication_login')
def account_edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profiles = ProfileForm(request.POST, instance=profile)
        if profiles.is_valid():
            profile_check = profiles.save(commit=False)
            profile_check.user = request.user
            profile_check.save()
            return redirect('account_profile')
        error = profiles.errors
        return render(request, "account_edit_profile.html",{"profile_form":profile_form, "error":error})
    return render(request, "account_edit_profile.html",{"profile_form":profile_form})
def billing_details(request):
    return render(request, "billing_details.html")

def blog_post(request):
    return render(request, "blog_post.html", {})

def blog_read(request):
    return render(request, "blog_read.html", {})

def cart(request):
    cart = Product.objects.filter(status_two = 3)
    product = Product.objects.all()
    context = {"carts":cart, "products":product}
    return render(request, "cart.html", context)

def contact_us(request):
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('thank_you')
        return redirect('contact_us')
    return render(request, "contact_us.html", {})

def payment_method(request):
    return render(request, "payment_method.html", {})

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product":product}
    return render(request, "product_details.html", context)

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
    products = Product.objects.filter(status=1)
    context = {"products":products}
    return render(request, "wishlist.html", context)

def address(request):
    return render(request, 'address.html' )

def wish_product(request, pk):
    wish = get_object_or_404(Product, pk=request.POST.get('product.id'))
    if wish.status == 0:
        wish.status = 1
        wish.save()
    else:
        wish.status = 0
        wish.save()
    return redirect('/')

def add_cart(request, pk):
    add = get_object_or_404(Product, pk= request.POST.get("product.id"))
    if add.status_two == 2:
        add.status_two = 3
        add.save()
    else:
        add.status_two = 2
        add.save()
    return redirect("/")

def remove_cart(request, pk):
    remove_item = Product.objects.get(id=pk)
    print(remove_item.status_two)
    if remove_item.status_two == 3:
        remove_item.status_two = 2
        remove_item.save()
        print(remove_item.status_two)
    return redirect('cart')