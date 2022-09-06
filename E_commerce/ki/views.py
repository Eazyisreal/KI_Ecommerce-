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

