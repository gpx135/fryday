from rest_framework import serializers
from .models import EmailTemplate, EmailTemplateTranslation

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

class EmailTemplateTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplateTranslation
        fields = '__all__'