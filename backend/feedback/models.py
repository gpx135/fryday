from django.db import models
from django.utils.translation import gettext_lazy as _


class Feedback(models.Model):
    """Stores user feedback."""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)
    comment = models.TextField(blank=True)
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedback")

    def __str__(self):
        return f"Feedback from {self.user.username}"

class ExternalReview(models.Model):
    """
    Model representing a review from an external platform.
    """
    id = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=50, null=False)  # Name of the review platform, e.g., 'Google Maps', 'Wolt', 'Foodora'
    external_review_id = models.CharField(max_length=255, null=False, unique=True)  # Unique ID provided by the third-party platform
    user = models.ForeignKey('users.User', null=True, blank=True, on_delete=models.SET_NULL)  # Reference to a user in the reviews app
    rating = models.IntegerField(null=False)  # Rating given by the user, e.g., 1 to 5
    comment = models.TextField(null=False)  # Review comment provided by the user
    response = models.TextField(null=True)  # Response to the review
    review_date = models.DateTimeField(null=False)  # Date when the review was created on the external platform
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the review was created in the local system
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the review was last updated in the local system

    def __str__(self):
        return f"{self.platform} Review - {self.external_review_id}"