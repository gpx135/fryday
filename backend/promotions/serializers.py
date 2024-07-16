from rest_framework import serializers
from .models import Promotion, PromotionTranslation, GiftCard

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionTranslation
        fields = '__all__'

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = '__all__'