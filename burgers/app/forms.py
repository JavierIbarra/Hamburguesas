from dataclasses import field
from http import client
from urllib import request
from django import forms
from .models import Event, Ingredient
import datetime

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ["title","address", "ingredients", "attendees", "start_date", "end_date"] 
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "ingredients": forms.SelectMultiple(
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
                attrs={"type": "datetime-local", "class": "form-control", "id":"start_date"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_date": forms.DateInput(
                attrs={"type": "datetime-local", "class": "form-control", "id":"end_date"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name","image", "unitary_cost"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "unitary_cost":forms.NumberInput(
                attrs={
                    "class": "form-control", 
                    "min": 0,
                }
            ),
        }