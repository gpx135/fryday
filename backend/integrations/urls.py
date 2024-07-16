from rest_framework.routers import DefaultRouter
from .views import APIIntegrationViewSet, SyncLogViewSet

router = DefaultRouter()
router.register(r'integrations', APIIntegrationViewSet)
router.register(r'synclogs', SyncLogViewSet)

urlpatterns = router.urls