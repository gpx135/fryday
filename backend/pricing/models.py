from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _



class BuffetPricing(models.Model):
    """Stores pricing information for buffet on different days and times."""
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = [
        (0, _('Sunday')), (1, _('Monday')), (2, _('Tuesday')),
        (3, _('Wednesday')), (4, _('Thursday')), (5, _('Friday')), (6, _('Saturday')),
    ]
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(start_time__lt=models.F('end_time')),
                                   name='start_time_before_end_time')
        ]
        verbose_name = _("Buffet Pricing")
        verbose_name_plural = _("Buffet Pricing")

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time}-{self.end_time}: ${self.price}"


class SpecialGroupPricing(models.Model):
    """Stores special pricing for user groups."""
    id = models.AutoField(primary_key=True)
    user_group = models.ForeignKey('users.UserGroup', on_delete=models.CASCADE)
    buffet_pricing = models.ForeignKey(BuffetPricing, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('user_group', 'buffet_pricing')
        verbose_name = _("Special Group Pricing")
        verbose_name_plural = _("Special Group Pricing")

    def __str__(self):
        return f"{self.user_group.name} - {self.buffet_pricing}"