from http import client
from urllib import request
from django import forms
from .models import Event
import datetime

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ["title","address", "attendees", "start_date", "end_date"] 
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "attendees": forms.NumberInput(
                attrs={
                    "class": "form-control", 
                    "min": 0,
                }
            ),
            "start_date": forms.DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_date": forms.DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }