from rest_framework import viewsets
from .models import (
    FoodCategory, FoodCategoryTranslation, FoodItem, FoodItemTranslation,
    DietaryPreference, DietaryPreferenceTranslation, FoodItemDietaryInfo
)
from .serializers import (
    FoodCategorySerializer, FoodCategoryTranslationSerializer, FoodItemSerializer,
    FoodItemTranslationSerializer, DietaryPreferenceSerializer,
    DietaryPreferenceTranslationSerializer, FoodItemDietaryInfoSerializer
)

class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

class FoodCategoryTranslationViewSet(viewsets.ModelViewSet):
    queryset = FoodCategoryTranslation.objects.all()
    serializer_class = FoodCategoryTranslationSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class FoodItemTranslationViewSet(viewsets.ModelViewSet):
    queryset = FoodItemTranslation.objects.all()
    serializer_class = FoodItemTranslationSerializer

class DietaryPreferenceViewSet(viewsets.ModelViewSet):
    queryset = DietaryPreference.objects.all()
    serializer_class = DietaryPreferenceSerializer

class DietaryPreferenceTranslationViewSet(viewsets.ModelViewSet):
    queryset = DietaryPreferenceTranslation.objects.all()
    serializer_class = DietaryPreferenceTranslationSerializer

class FoodItemDietaryInfoViewSet(viewsets.ModelViewSet):
    queryset = FoodItemDietaryInfo.objects.all()
    serializer_class = FoodItemDietaryInfoSerializer