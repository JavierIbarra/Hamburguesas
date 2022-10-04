from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    email = models.EmailField(max_length=200,)

    def __str__(self):
        return str(self.user)

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    admin_name = models.CharField(max_length=30, null=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    email = models.EmailField(max_length=200,)

    def __str__(self):
        return str(self.user)