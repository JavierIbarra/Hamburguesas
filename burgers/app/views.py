from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import ReservationForm, EventForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class ListReservationView(ListView):
    model = Reservation
    template_name = 'event/calendar.html'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            user_client=Client.objects.filter(user=self.request.user)
            queryset = self.model.objects.filter(state=True, client=user_client[0])
        else:
            queryset = self.model.objects.none()
        return queryset

class ListEventView(ListView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('app:calendar')

class CreateEventView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('app:calendar')

class UpdateEventView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('app:calendar')

class DeleteEventView(DeleteView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('app:calendar')

class CreaterReservationView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'event/create_reservation.html'
    success_url = reverse_lazy('app:create_event')