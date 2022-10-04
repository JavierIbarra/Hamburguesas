from django import forms
from .models import Reservation, Event
import datetime


class ReservationForm(forms.ModelForm):
    start_date = forms.DateTimeField(label='Start', initial=datetime.date.today)
    end_date = forms.DateTimeField(label='End', initial=datetime.date.today)

    class Meta:
        model = Reservation
        fields = ["start_date", "end_date"]

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ["address", "attendees"]