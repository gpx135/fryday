from django.contrib import admin
from .models import Promotion, PromotionTranslation, GiftCard

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percent', 'start_date', 'end_date', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'start_date', 'end_date')

@admin.register(PromotionTranslation)
class PromotionTranslationAdmin(admin.ModelAdmin):
    list_display = ('promotion', 'language', 'name')
    search_fields = ('promotion__name', 'language__code', 'name')

@admin.register(GiftCard)
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('code', 'balance', 'initial_balance', 'user', 'is_active', 'expiry_date')
    search_fields = ('code', 'user__username')
    list_filter = ('is_active', 'expiry_date')