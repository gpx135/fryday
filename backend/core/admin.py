from django.contrib import admin
from .models import OpeningHours, SpecialClosure

@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'open_time', 'close_time', 'is_closed')
    list_filter = ('day_of_week', 'is_closed')
    search_fields = ('day_of_week',)

@admin.register(SpecialClosure)
class SpecialClosureAdmin(admin.ModelAdmin):
    list_display = ('date', 'reason')
    search_fields = ('date', 'reason')