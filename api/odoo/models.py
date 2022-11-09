from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from usermanager.models import Client
from app.models import Event
from .utils import Odoo

