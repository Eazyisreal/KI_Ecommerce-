from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ki.forms import ProfileForm, ContactForm
from ki.models import Profile, Contact, Product, Category, Cart


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
    product_new = Product.objects.filter(category__category__contains = "new_arrival")
    best_selling = Product.objects.filter(category__category__contains="Best Selling")
    trending = Product.objects.filter(category__category__contains="Trending")
    special_offer = Product.objects.filter(category__category__contains="Special Offer")
    # trending = Product.objects.filter(category__category__contains="trending")
    context = {"products":products, "product_new":product_new, "best_selling":best_selling, "trending":trending, "special_offer":special_offer}
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

@login_required(login_url='authentication_login')
def cart(request):
    cart = Product.objects.filter(username=request.user, status_two=3)
    context = {"carts":cart}
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
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"categories":categories, "products":products}
    return render(request, "shop_grid.html", context)


def thank_you(request):
    return render(request, "thank_you.html", {})

def wishlist(request):
    products = Product.objects.filter(username=request.user, status=1)
    context = {"products":products}
    return render(request, "wishlist.html", context)

def address(request):
    return render(request, 'address.html' )

def wish_product(request, pk):
    wish = get_object_or_404(Product, pk=request.POST.get('product.id'))
    wish.username.add(request.user)
    if wish.status == 0:
        wish.status = 1
        wish.save()
    else:
        wish.status = 0
        wish.save()
    return redirect('/')

def add_cart(request, pk):
    cart = get_object_or_404(Product, pk=request.POST.get('product.id'))
    cart.username.add(request.user)
    if cart.status_two == 2:
        cart.status_two = 3
        cart.save()
    else:
        cart.status_two = 2
        cart.save()
    return redirect('/')
def remove_cart(request, pk):
    remove_item = Product.objects.get(id=pk)
    print(remove_item.status_two)
    if remove_item.status_two == 3:
        remove_item.status_two = 2
        remove_item.save()
        print(remove_item.status_two)
    return redirect('cart')