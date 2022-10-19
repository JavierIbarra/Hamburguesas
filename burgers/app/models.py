from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from usermanager.models import Client
 

class Event(models.Model):
    title = models.CharField(max_length = 200, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.BooleanField(default=True)
    address = models.CharField(max_length=200, null=False)
    attendees = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)])
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Ingredient(models.Model):
    KILOGRAMS = 'Kg'
    GRAMS = 'gr'
    LITERS = 'Lts'
    UNIT = 'Unt'
    MEASUREMENT_CHOICES = [
        (KILOGRAMS, 'Kilograms'),
        (GRAMS, 'Grams'),
        (LITERS, 'Liters'),
        (UNIT, 'Unitary'),
    ]

    name = models.CharField(max_length=200, null=False)
    image = models.URLField()
    measurement = models.CharField(max_length=3, choices=MEASUREMENT_CHOICES, default=KILOGRAMS)
    unitary_cost = models.IntegerField(validators=[MinValueValidator(0)])
    avg_consumption_pp = models.FloatField()


    def __str__(self):
        return str(self)

class OrderItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.ingredient.unitary_cost * self.quantity
        return total 
