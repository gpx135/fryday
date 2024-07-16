from django.contrib import admin
from .models import Feedback, ExternalReview

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'upvote', 'downvote', 'created_at')
    search_fields = ('user__username', 'comment', 'response')
    list_filter = ('created_at',)

@admin.register(ExternalReview)
class ExternalReviewAdmin(admin.ModelAdmin):
    list_display = ('platform', 'external_review_id', 'user', 'rating', 'review_date', 'created_at')
    search_fields = ('platform', 'external_review_id', 'user__username')
    list_filter = ('platform', 'rating', 'review_date')