from django.contrib import admin
from .models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = 'pk', 'number', 'place_count'
    list_display_links = "pk", "number"
    ordering = "-number",
    search_fields = 'number',


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = 'pk', 'date_time', 'duration', 'client_info'
    ordering = ("date_time",)
    search_fields = 'pk', 'date_time', 'client_info'
