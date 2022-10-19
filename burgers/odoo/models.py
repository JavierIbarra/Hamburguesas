from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from usermanager.models import Client
from app.models import Event
from .utils import Odoo

@receiver(post_save, sender=Client)
def create_client_odoo(sender, instance, created, **kwargs):
    if created:
        od = Odoo()
        od.authenticateOdoo()
        partnerRow = [{"name":instance.first_name +" "+ instance.last_name, "phone":instance.phone, "email":instance.email}]
        od.partnerAdd(partnerRow)

@receiver(post_save, sender=Event)
def create_crm_odoo(sender, instance, created, **kwargs):
    if created:
        pass
    pass