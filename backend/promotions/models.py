from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    """Stores promotion information."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount_percent = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    min_purchase_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)]
    )
    max_discount_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lte=models.F('end_date')),
                name='start_date_before_end_date'
            )
        ]
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return self.name

class PromotionTranslation(models.Model):
    """Stores translations for promotions."""
    id = models.AutoField(primary_key=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    language = models.ForeignKey('localization.Language', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('promotion', 'language')
        verbose_name = _("Promotion Translation")
        verbose_name_plural = _("Promotion Translations")

    def __str__(self):
        return f"{self.promotion.name} - {self.language.code}"

class GiftCard(models.Model):
    """Stores gift card information."""
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    expiry_date = models.DateField(null=True, blank=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['is_active']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(balance__lte=models.F('initial_balance')),
                name='balance_less_than_or_equal_to_initial'
            )
        ]
        verbose_name = _("Gift Card")
        verbose_name_plural = _("Gift Cards")

    def __str__(self):
        return f"Gift Card {self.code}"
