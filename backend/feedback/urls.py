from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet, ExternalReviewViewSet

router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'external-reviews', ExternalReviewViewSet)

urlpatterns = router.urls