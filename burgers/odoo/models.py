from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from usermanager.models import Client
from app.models import Event
import requests


@receiver(post_save, sender=Client)
def create_client_odoo(sender, instance, created, **kwargs):
    if created and not instance.is_superuser :
        json_sent = {"name":instance.first_name +" "+ instance.last_name, 
                        "phone":instance.phone, 
                        "email":instance.email}

        requests.post("http://api-flask:5000/contact/add", json = json_sent)

@receiver(post_save, sender=Event)
def create_crm_odoo(sender, instance, created, **kwargs):
    if created:
        partnerEmail = {'partnerEmail': instance.client.email}
        user_id = requests.post("http://api-flask:5000/partner", json = partnerEmail)
        
        costo = 1000 * int(instance.attendees)

        json_sent = {
                        "name": instance.title, 
                        "burger": instance.attendees, 
                        "partner_id": f'{user_id.json()["id"]}',
                        "phone": instance.client.phone,
                        "street": instance.address,
                        "expected_revenue": f'{costo}',
                    }

        
                    
        requests.post("http://api-flask:5000/crm/add", json = json_sent)

