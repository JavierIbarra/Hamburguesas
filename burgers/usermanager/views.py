from .forms import LoginForm, SignUpForm
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def signout(request):
    logout(request)
    return redirect("login")


class LoginView(View):

    template_name = "usermanager/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


class SignUpView(View):

    template_name = "usermanager/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("login")
        context = {"form": forms}
        return render(request, self.template_name, context)
