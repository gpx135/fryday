from django.db import models
from django.utils.translation import gettext_lazy as _


class AuditTrail(models.Model):
    """Stores audit trail information for database changes."""
    id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    record_id = models.PositiveIntegerField()
    action = models.CharField(max_length=10, choices=[
        ('INSERT', 'Insert'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete')
    ])
    old_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)
    changed_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=100, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['table_name', 'record_id']),
            models.Index(fields=['changed_at']),
        ]
        verbose_name = _("Audit Trail")
        verbose_name_plural = _("Audit Trails")

    def __str__(self):
        return f"{self.action} on {self.table_name} (ID: {self.record_id})"