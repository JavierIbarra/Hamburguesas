from dataclasses import field
from http import client
from tkinter import Widget
from urllib import request
from django import forms
from .models import Event, Ingredient
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

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name","image","measurement","unitary_cost","avg_consumption_pp"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "image": forms.FileInput(
                attrs={"class": "form-control"}
            ),
            "measurement": forms.Select(
                attrs={
                    "choice": "Kg", 
                    "class":"form-control", 
                    "choices": Ingredient.MEASUREMENT_CHOICES
                    }
            ),
            "unitary_cost":forms.NumberInput(
                attrs={
                    "class": "form-control", 
                    "min": 0,
                }
            ),
            "avg_consumption_pp":forms.NumberInput(
                attrs={
                    "class": "form-control", 
                    "min": 0,
                }
            ),
        }