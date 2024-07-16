from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsletterContact(models.Model):
    """Stores newsletter contact information."""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("Newsletter Contact")
        verbose_name_plural = _("Newsletter Contacts")

    def __str__(self):
        return self.email

class ContactFormSubmission(models.Model):
    """Stores contact form submissions."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Contact Form Submission")
        verbose_name_plural = _("Contact Form Submissions")

    def __str__(self):
        return f"Contact from {self.name}"
