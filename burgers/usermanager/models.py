from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
"""
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
"""

class Client(AbstractBaseUser):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200,)
    image = models.URLField(null=False, blank=False)
    user_active = models.BooleanField(default=True)
    user_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name}.{self.last_name}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_admin