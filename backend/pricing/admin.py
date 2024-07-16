from django.contrib import admin
from .models import BuffetPricing, SpecialGroupPricing

@admin.register(BuffetPricing)
class BuffetPricingAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'end_time', 'price')
    search_fields = ('day_of_week',)
    list_filter = ('day_of_week',)

@admin.register(SpecialGroupPricing)
class SpecialGroupPricingAdmin(admin.ModelAdmin):
    list_display = ('user_group', 'buffet_pricing', 'price')
    search_fields = ('user_group__name', 'buffet_pricing__day_of_week')
    list_filter = ('user_group',)