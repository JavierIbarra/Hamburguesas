from contextlib import nullcontext
from email.policy import default
from itertools import count
from operator import mod
from pyexpat import model
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from usermanager.models import Client
 
class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.URLField(null=True, blank =True)
    unitary_cost = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.name) + " $" + str(self.unitary_cost) + " cost per unit." 


class Event(models.Model):
    MEASUREMENT_CHOICES = [
        ('Created', 'created'),
        ('Accepted', 'accepted'),
        ('Cancelled', 'cancelled'),
        ('Finalized', 'finalized'),
    ]
    title = models.CharField(max_length = 200, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=MEASUREMENT_CHOICES, default='Created')
    address = models.CharField(max_length=200, null=False)
    attendees = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)])
    creation = models.DateTimeField(auto_now_add=True)

    def costo_total(self):
        costo = 1000 * self.attendees
        for ingredient in self.ingredients.all():
            costo += ingredient.unitary_cost * self.attendees
        return costo

    def __str__(self):
        return str(self.title)