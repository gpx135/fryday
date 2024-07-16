from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):
    """Stores frequently asked questions."""
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    order_index = models.IntegerField(default=0)

    class Meta:
        ordering = ['order_index', 'id']
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question[:50]

class FAQTranslation(models.Model):
    """Stores translations for FAQs."""
    id = models.AutoField(primary_key=True)
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    language = models.ForeignKey('localization.Language', on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)

    class Meta:
        unique_together = ('faq', 'language')
        verbose_name = _("FAQ Translation")
        verbose_name_plural = _("FAQ Translations")

    def __str__(self):
        return f"{self.faq.question[:30]} - {self.language.code}"

