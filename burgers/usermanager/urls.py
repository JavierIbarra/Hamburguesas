from django.urls import path
from . import views as usermanager
from .views import SingUpView
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    #path('', RedirectView.as_view(url='/accounts/login/')),
    #path('',app.home, name='home'),
    #path('login', usermanager.loginMethod, name='login'),
    #path('registration', usermanager.registration, name='registration'),
    #path('logout', usermanager.logoutMethod,name='logout'),

    path('signup/', SingUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(template_name="usermanager/login.html"), name="login"),
    path('logout/', logout_then_login, name="logout"),
]