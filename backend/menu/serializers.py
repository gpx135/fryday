from rest_framework import serializers
from .models import (
    FoodCategory, FoodCategoryTranslation, FoodItem, FoodItemTranslation,
    DietaryPreference, DietaryPreferenceTranslation, FoodItemDietaryInfo
)

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

class FoodCategoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategoryTranslation
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class FoodItemTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemTranslation
        fields = '__all__'

class DietaryPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryPreference
        fields = '__all__'

class DietaryPreferenceTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryPreferenceTranslation
        fields = '__all__'

class FoodItemDietaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItemDietaryInfo
        fields = '__all__'