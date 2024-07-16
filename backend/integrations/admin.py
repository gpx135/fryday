from django.contrib import admin
from .models import APIIntegration, SyncLog

@admin.register(APIIntegration)
class APIIntegrationAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'sync_enabled', 'last_synced_at')
    search_fields = ('service_name',)

@admin.register(SyncLog)
class SyncLogAdmin(admin.ModelAdmin):
    list_display = ('integration', 'sync_type', 'status', 'synced_at')
    search_fields = ('integration__service_name', 'sync_type', 'status')