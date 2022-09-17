import email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ki.forms import ProfileForm, ContactForm
from ki.models import Profile, Contact

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



def account_orders(request):
    return render(request, "account_orders.html", {})

@login_required(login_url='authentication_login')
def account_profile(request):
    profile = Profile.objects.get(user__email = request.user.email)
    context = {"profile":profile}
    return render(request, 'account_profile.html', context)

@login_required(login_url='authentication_login')
def create_profile(request):
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form_add = form.save(commit=False)
            form_add.user = request.user
            form_add.save()
            return redirect('/')
        else:
            print(form.errors)
    profile_form = ProfileForm()
    return render(request, "account_edit_profile.html", {"profile_form":profile_form})

@login_required(login_url='authentication_login')
def account_edit(request, pk):
    profile = Profile.objects.get(id=pk)
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profiles = ProfileForm(request.POST, instance=profile)
        if profiles.is_valid():
            profile_check = profiles.save(commit=False)
            profile_check.user = request.user
            profile_check.save()
            return redirect('account_profile')
        else:
            err = (profiles.errors)
            print(err)
            return render(request, "text.html",{"profile_form":profile_form, "errors":err})
    return render(request, "text.html",{"profile_form":profile_form})
def billing_details(request):
    return render(request, "billing_details.html")

def blog_post(request):
    return render(request, "blog_post.html", {})

def blog_read(request):
    return render(request, "blog_read.html", {})

def cart(request):
    return render(request, "cart.html", {})

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

def address(request):
    return render(request, 'address.html' )




