from rest_framework.routers import DefaultRouter
from .views import OpeningHoursViewSet, SpecialClosureViewSet

router = DefaultRouter()
router.register(r'opening-hours', OpeningHoursViewSet)
router.register(r'special-closures', SpecialClosureViewSet)

urlpatterns = router.urls