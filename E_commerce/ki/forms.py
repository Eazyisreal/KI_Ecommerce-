from django import forms
from ki.models import Profile, Contact

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'location', 'phone_number',
        'date_of_birth', 'user_image')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"