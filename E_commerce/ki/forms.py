from django import forms
from ki.models import MyUser
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email',)