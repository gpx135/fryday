from django.contrib import admin
from .models import EmailTemplate, EmailTemplateTranslation

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_html', 'created_at')
    search_fields = ('name', 'subject')
    list_filter = ('is_html', 'created_at')

@admin.register(EmailTemplateTranslation)
class EmailTemplateTranslationAdmin(admin.ModelAdmin):
    list_display = ('email_template', 'language_id', 'subject')
    search_fields = ('email_template__name', 'subject')
    list_filter = ('language_id',)