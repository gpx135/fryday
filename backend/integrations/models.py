from django.db import models

class APIIntegration(models.Model):
    """
    Model representing an integration with a third-party API service.
    """
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100, null=False)  # Name of the service, e.g., 'Google Maps', 'DeliveryApp1'
    api_key = models.CharField(max_length=255, null=False)  # API key for authenticating requests to the service
    sync_enabled = models.BooleanField(default=True)  # Flag to enable or disable synchronization
    sync_opening_hours = models.BooleanField(default=False)  # Flag to enable synchronization of opening hours
    sync_menu = models.BooleanField(default=False)  # Flag to enable synchronization of the menu
    sync_promotions = models.BooleanField(default=False)  # Flag to enable synchronization of promotions
    sync_frequency = models.DurationField(null=True)  # Interval for how often to sync
    retry_attempts = models.IntegerField(default=3)  # Number of retry attempts for synchronization failures
    last_synced_at = models.DateTimeField(null=True)  # Timestamp of the last successful synchronization

    def __str__(self):
        return self.service_name

class SyncLog(models.Model):
    """
    Model representing a log entry for synchronization attempts with third-party API services.
    """
    id = models.AutoField(primary_key=True)
    integration = models.ForeignKey(APIIntegration, on_delete=models.CASCADE)  # Reference to the API integration
    sync_type = models.CharField(max_length=50, null=False)  # Type of synchronization, e.g., 'opening_hours', 'menu', 'promotions'
    status = models.CharField(max_length=20, null=False)  # Status of the sync attempt, e.g., 'success', 'failure'
    message = models.TextField()  # Detailed message about the sync attempt
    synced_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the sync attempt occurred

    def __str__(self):
        return f"{self.integration.service_name} - {self.sync_type} - {self.status}"