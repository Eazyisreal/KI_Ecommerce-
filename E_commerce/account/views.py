from django.shortcuts import render, redirect
from account.forms import MyUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.


def signup_user(request):
    form = MyUserForm()
    if request.method == "POST":
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "You have registered successful")
            return redirect('authentication_login')
        else:
            messages.info(request, "invalid input. please try again")
            return redirect('signup_user')
    context = {'form':form}
    return render(request, 'authentication_register.html', context)

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
            messages.info(request, "invalid input. Input the correct information")
            return redirect('authetication_login')
    return render(request, "authentication_login.html", {})


def authentication_reset_password(request):
    return render(request, "authentication_reset_password.html", {})

def logout_user(request):
    logout(request)
    return redirect('authentication_login')