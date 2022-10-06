from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Client


class LoginYSuperStaffMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('home')

class LoginMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')

class ValidarPermisosMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str): return (self.permission_required)
        else: return self.permission_required

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, "You do not have permissions to perform this action.")
        return redirect(self.get_url_redirect())

class LoginClientMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            clt = Client.objects.filter(user=self.request.user)
            if len(clt) > 0:
                return super().dispatch(request, *args, **kwargs)
        return redirect('home')