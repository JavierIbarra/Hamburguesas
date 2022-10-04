from django.contrib import admin
from .models import Event, Reservation

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ("address","reservation")


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("client", "start_date", "end_date")

admin.site.register(Event, EventAdmin)
admin.site.register(Reservation, ReservationAdmin)