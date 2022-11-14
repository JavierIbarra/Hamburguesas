from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('calendar/', EventsCalendarView.as_view(), name='calendar'),
    path('events/', ListEventView.as_view(), name='list_event'),
    path('events/add/', CreateEventView.as_view(), name='create_event'),
    path('<int:pk>/update/',UpdateEventView.as_view(), name='update_event'),
    path('<int:pk>/delete/',DeleteEventView.as_view(), name='delete_event'),
    path('ingredients/', ListIngredientView.as_view(), name='ingredients'),
    path('ingredients/add/',CreateIngredientView.as_view(), name='create_ingredient'),
    #path('<int:pk>/update/',UpdateIngredientView.as_view(), name='update_ingredient'),
    #path('<int:pk>/delete/',DeleteIngredientView.as_view(), name='delete_ingredient'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)