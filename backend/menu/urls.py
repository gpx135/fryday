from rest_framework.routers import DefaultRouter
from .views import (
    FoodCategoryViewSet, FoodCategoryTranslationViewSet, FoodItemViewSet,
    FoodItemTranslationViewSet, DietaryPreferenceViewSet,
    DietaryPreferenceTranslationViewSet, FoodItemDietaryInfoViewSet
)

router = DefaultRouter()
router.register(r'food-categories', FoodCategoryViewSet)
router.register(r'food-category-translations', FoodCategoryTranslationViewSet)
router.register(r'food-items', FoodItemViewSet)
router.register(r'food-item-translations', FoodItemTranslationViewSet)
router.register(r'dietary-preferences', DietaryPreferenceViewSet)
router.register(r'dietary-preference-translations', DietaryPreferenceTranslationViewSet)
router.register(r'food-item-dietary-info', FoodItemDietaryInfoViewSet)

urlpatterns = router.urls