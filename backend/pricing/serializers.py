from rest_framework import serializers
from .models import BuffetPricing, SpecialGroupPricing

class BuffetPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuffetPricing
        fields = '__all__'

class SpecialGroupPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialGroupPricing
        fields = '__all__'
