
from django.contrib import admin
from .models import FAQ, FAQTranslation

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'order_index')
    search_fields = ('question', 'category')
    list_filter = ('category',)
    ordering = ('order_index', 'id')

@admin.register(FAQTranslation)
class FAQTranslationAdmin(admin.ModelAdmin):
    list_display = ('faq', 'language')
    search_fields = ('faq__question', 'language__code')
    list_filter = ('language',)