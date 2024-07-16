from rest_framework import serializers
from .models import Feedback, ExternalReview

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ExternalReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalReview
        fields = '__all__'