from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin,)
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        if not email:  
            raise AttributeError("User must set an email address")
        else:  
            email = self.normalize_email(email)

        # create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)  
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class Client(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
    )
    phone = models.IntegerField(validators=[MaxValueValidator(999999999), MinValueValidator(100000000)], null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
