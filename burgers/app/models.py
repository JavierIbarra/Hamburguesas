from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from usermanager.models import Client

# Create your models here.
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.BooleanField(default=True)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.client) +" "+ str(self.start_date)
 

class Event(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=False)
    attendees = models.IntegerField(validators=[MaxValueValidator(1000), MinValueValidator(0)])

    def __str__(self):
        return str(self.reservation)


class Ingredients(models.Model):
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
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    measurement = models.CharField(max_length=3, choices=MEASUREMENT_CHOICES, default=KILOGRAMS)
    unitary_cost = models.IntegerField(validators=[MinValueValidator(0)])


    def __str__(self):
        return str(self)

class Catalogue(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return str(self)
