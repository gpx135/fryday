
from rest_framework.routers import DefaultRouter
from .views import AuditTrailViewSet

router = DefaultRouter()
router.register(r'audit-trails', AuditTrailViewSet)

urlpatterns = router.urls