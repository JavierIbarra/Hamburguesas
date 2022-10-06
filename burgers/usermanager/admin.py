from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ("date_joined", "email", "phone",)

admin.site.register(Client, ClientAdmin)