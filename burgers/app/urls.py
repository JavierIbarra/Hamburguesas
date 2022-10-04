from django.urls import path
from .views import *

urlpatterns = [
    #path('', RedirectView.as_view(url='/accounts/login/')),
    path('', HomePageView.as_view(), name='home'),
    path('calendar/', ListReservationView.as_view(), name='calendar'),
    path('reservation/', CreaterReservationView.as_view(), name='create_reservation'),
    path('events/', ListEventView.as_view(), name='list_event'),
    path('profile/', HomePageView.as_view(), name='profile'),
]