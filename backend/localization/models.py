from django.db import models
from django.utils.translation import gettext_lazy as _


class Language(models.Model):
    """Stores supported languages for internationalization."""
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        indexes = [models.Index(fields=['code'])]
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return f"{self.name} ({self.code})"