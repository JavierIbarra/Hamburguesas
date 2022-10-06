from http import client
from urllib import request
from django import forms
from .models import Event
import datetime

class EventForm(forms.ModelForm):
    start_date = forms.DateTimeField(label='Start', initial=datetime.date.today)
    end_date = forms.DateTimeField(label='End', initial=datetime.date.today)

    class Meta:
        model = Event
        fields = ["address", "attendees", "start_date", "end_date"] 