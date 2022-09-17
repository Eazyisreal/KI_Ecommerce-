from accs.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class MyUserForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(max_length =255, help_text='Required, Please add valid E-mail Address', required=True)
        model = MyUser
        fields = ('email','password1', 'password2')

        
    def __init__(self, *args, **kwargs):
        
        super(MyUserForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password1'],self.fields['password2']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        #verifying that the email hasn't been previously registered
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already in use")
        return email

    def clean_password2(self):
       # Check that the two password entries match
       password1 = self.cleaned_data.get("password1")
       password2 = self.cleaned_data.get("password2")
       if password1 and password2 and password1 != password2:
           raise ValidationError("Passwords don't match")
       return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            return user