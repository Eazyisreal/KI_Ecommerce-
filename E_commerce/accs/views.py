from django.shortcuts import render, redirect
from accs.forms import MyUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def signup_user(request):
    user_form = MyUserForm()
    context = {'user_form':user_form}
    if request.method == "POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, "registration successful")
            return redirect('/')
        error = form.errors
        context = {'error':error}
        return render(request, 'accounts/authentication_register.html', context)
    return render(request, 'accounts/authentication_register.html', context)

def authentication_login(request):
    if request.method == 'POST':
        user = MyUserForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "invalid input. Input the correct information")
            return redirect('authentication_login')
    return render(request, "accounts/authentication_login.html", {})


def authentication_reset_password(request):
    return render(request, "authentication_reset_password.html", {})

def logout_user(request):
    logout(request)
    return redirect('authentication_login')