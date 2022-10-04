from django.urls import path
from .views import home

urlpatterns = [
    #path('', RedirectView.as_view(url='/accounts/login/')),
    path('', home, name='home'),
]