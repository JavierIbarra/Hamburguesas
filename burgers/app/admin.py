from django.contrib import admin
from .models import Event, Ingredient

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ("address",  "start_date", "end_date")

admin.site.register(Event, EventAdmin)
admin.site.register(Ingredient)