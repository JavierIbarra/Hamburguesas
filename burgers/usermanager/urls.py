from django.urls import path
from . import views as usermanager

urlpatterns = [
    #path('', RedirectView.as_view(url='/accounts/login/')),
    #path('',app.home, name='home'),
    path('login', usermanager.loginMethod, name='login'),
    path('registration', usermanager.registration, name='registration'),
    path('logout', usermanager.logoutMethod,name='logout'),
]