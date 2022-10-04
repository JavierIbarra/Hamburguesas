from cProfile import label
#from multiprocessing.connection import Client
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client, Administrator
from django import forms

class NewClientForm(UserCreationForm):  
    #TODO: Check both methods.
    #first_name = forms.CharField(label='First Name', max_length=200)
    #last_name = forms.CharField(label='Last Name', max_length=200)
    #phone = forms.IntegerField(label='Phone Number', validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    #email = forms.EmailField(label='Email', max_length=200)
    #password1: forms.PasswordInput(label='Password')
    #password2: forms.PasswordInput(label='Confirm Password')
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone', 'email', 'password1', 'password2']

class LoginClientForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=200)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())