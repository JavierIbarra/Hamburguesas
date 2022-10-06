from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from usermanager.mixins import LoginYSuperStaffMixin, ValidarPermisosMixin, LoginMixin
from .forms import EventForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class ProfilePageView(LoginMixin,ListView):
    template_name = "client/profile.html"
    model = Event 
    context_object_name = 'events'

    def get_queryset(self):
        queryset = self.model.objects.filter(state=True, client=self.request.user)
        return queryset


class EventsCalendarView(LoginMixin,ListView):
    model = Event
    template_name = 'event/calendar.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(state=True, client=self.request.user)
        return queryset

class ListEventView(LoginMixin, ListView):
    template_name = 'event/events.html'
    model = Event
    context_object_name = 'event_list'
    

class CreateEventView(LoginMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = reverse_lazy('list_event')

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class UpdateEventView(LoginMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'event/update_event.html'
    success_url = reverse_lazy('list_event')

class DeleteEventView(LoginMixin, DeleteView):
    model = Event
    template_name = 'event/event_confirm_delete.html'
    success_url = reverse_lazy('list_event')