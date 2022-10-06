from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('calendar/', EventsCalendarView.as_view(), name='calendar'),
    path('events/', ListEventView.as_view(), name='list_event'),
    path('events/add/', CreateEventView.as_view(), name='create_event'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('<int:pk>/update/',UpdateEventView.as_view(), name='update_event'),
    path('<int:pk>/delete/',DeleteEventView.as_view(), name='delete_event')
]