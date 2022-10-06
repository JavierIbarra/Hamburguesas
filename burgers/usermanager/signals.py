from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from usermanager.models import Client

@receiver(post_save, sender=User)
def create_user_client(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client(sender, instance, **kwargs):
    if not instance.is_superuser:
        instance.client.save()