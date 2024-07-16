from rest_framework.routers import DefaultRouter
from .views import BuffetPricingViewSet, SpecialGroupPricingViewSet

router = DefaultRouter()
router.register(r'buffet-pricings', BuffetPricingViewSet)
router.register(r'special-group-pricings', SpecialGroupPricingViewSet)

urlpatterns = router.urls