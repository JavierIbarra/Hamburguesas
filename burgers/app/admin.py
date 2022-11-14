from django.contrib import admin
from .models import Event, Ingredient

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ("address",  "start_date", "end_date")

class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "unitary_cost"]

admin.site.register(Event, EventAdmin)
admin.site.register(Ingredient, IngredientAdmin)