
from rest_framework import serializers
from .models import FAQ, FAQTranslation

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQTranslation
        fields = '__all__'