from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _



class Reservation(models.Model):
    """Stores reservation information."""
    id = models.AutoField(primary_key=True)
    class Status(models.TextChoices):
        PENDING = 'PE', _('Pending')
        CONFIRMED = 'CO', _('Confirmed')
        CANCELLED = 'CA', _('Cancelled')

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    special_requests = models.TextField(blank=True)
    table_number = models.CharField(max_length=20, blank=True)
    area = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['date', 'time']),
            models.Index(fields=['status']),
        ]
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"
