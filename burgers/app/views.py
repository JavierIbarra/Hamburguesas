from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .forms import EventForm
from usermanager.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginMixin, LoginClientMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class ListReservationView(LoginClientMixin,ListView):
    model = Event
    template_name = 'event/calendar.html'

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            user_client=Client.objects.filter(user=self.request.user)
            queryset = self.model.objects.filter(state=True, client=user_client[0])
        else:
            queryset = self.model.objects.none()
        return queryset

class ListEventView(LoginClientMixin,ListView):
    template_name = 'event/events.html'
    model = Event
    context_object_name = 'event_list'
    

class CreateEventView(LoginClientMixin,CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        if not self.request.user.is_anonymous:
            form.instance.client = Client.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)

class UpdateEventView(LoginClientMixin,UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event/update_event.html'
    success_url = reverse_lazy('calendar')

class DeleteEventView(LoginClientMixin,DeleteView):
    model = Event
    template_name = 'event/event_confirm_delete.html'
    success_url = reverse_lazy('calendar')