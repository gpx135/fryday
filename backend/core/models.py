from django.db import models
from django.utils.translation import gettext_lazy as _


class OpeningHours(models.Model):
    """Stores restaurant opening hours."""
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = [
        (0, _('Sunday')), (1, _('Monday')), (2, _('Tuesday')),
        (3, _('Wednesday')), (4, _('Thursday')), (5, _('Friday')), (6, _('Saturday')),
    ]
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    open_time = models.TimeField()
    close_time = models.TimeField()
    is_closed = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(open_time__lt=models.F('close_time')),
                                   name='open_time_before_close_time')
        ]
        verbose_name = _("Opening Hours")
        verbose_name_plural = _("Opening Hours")

    def __str__(self):
        return f"{self.get_day_of_week_display()}: {self.open_time}-{self.close_time}"

class SpecialClosure(models.Model):
    """Stores information about special closure dates."""
    id = models.AutoField(primary_key=True)
    date = models.DateField(unique=True)
    reason = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _("Special Closure")
        verbose_name_plural = _("Special Closures")

    def __str__(self):
        return f"{self.date}: {self.reason}"
