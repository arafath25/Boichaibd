from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'companyname', 'email', 'phone', 'country', 'address1', 'address2', 'town',
                  'state', 'postcode', 'password1', 'password2']
