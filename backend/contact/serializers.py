from rest_framework import serializers
from .models import NewsletterContact, ContactFormSubmission

class NewsletterContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterContact
        fields = '__all__'

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = '__all__'