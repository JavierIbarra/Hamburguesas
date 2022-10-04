import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models.signals import post_save

#from .forms import NewClientForm, LoginClientForm
#from .models import Client, Administrator


from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

#TODO:Check Decorators
# Create your views here.

"""
def loginMethod(request):
    login_form = LoginClientForm()
    if request.method == "POST":
        login_form = LoginClientForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, 
                                username=login_form.cleaned_data.get('email'), 
                                password=login_form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged')
                return(redirect('home'))
        messages.error(request, 'Failed Login')
        return(redirect('login'))

    context = { "login_form" : login_form}
    return(render(request, 'login.html', context=context))

def registration(request):
	if request.method == "POST":
		form = NewClientForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewClientForm()
	return render (request=request, template_name="registration.html", context={"form":form})

def logoutMethod(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    context = {}
    return(redirect('login'))
"""

class SingUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'usermanager/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2'})
        form.fields['username'].help_text  = ""
        form.fields['email'].help_text  = ""
        form.fields['password1'].help_text = ""
        form.fields['password2'].help_text  = ""
        return form
