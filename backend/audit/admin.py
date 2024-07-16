from django.contrib import admin
from .models import AuditTrail

@admin.register(AuditTrail)
class AuditTrailAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'record_id', 'action', 'changed_by', 'changed_at')
    search_fields = ('table_name', 'action', 'changed_by__username')
    list_filter = ('action', 'changed_at')