from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet, PromotionTranslationViewSet, GiftCardViewSet

router = DefaultRouter()
router.register(r'promotions', PromotionViewSet)
router.register(r'promotion-translations', PromotionTranslationViewSet)
router.register(r'gift-cards', GiftCardViewSet)

urlpatterns = router.urls