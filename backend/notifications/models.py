from django.db import models

class EmailTemplate(models.Model):
    """
    Model representing an email template used for various notifications.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True)  # Unique name of the email template, e.g., 'sign_up_confirmation'
    subject = models.CharField(max_length=255, null=False)  # Subject of the email
    body = models.TextField(null=False)  # Body content of the email
    is_html = models.BooleanField(default=True)  # Flag indicating if the email body is in HTML format
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the template was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the template was last updated

    def __str__(self):
        return self.name

class EmailTemplateTranslation(models.Model):
    """
    Model representing translations for email templates in different languages.
    """
    id = models.AutoField(primary_key=True)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)  # Reference to the email template
    language_id = models.IntegerField()  # Language ID for the translation, replace with ForeignKey(Language, on_delete=models.CASCADE) if Language model exists
    subject = models.CharField(max_length=255, null=False)  # Translated subject of the email
    body = models.TextField(null=False)  # Translated body content of the email

    def __str__(self):
        return f"{self.email_template.name} - {self.language_id}"