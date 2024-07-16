from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'party_size', 'status', 'table_number', 'area', 'created_at')
    search_fields = ('user__username', 'date', 'status')
    list_filter = ('status', 'date', 'created_at')