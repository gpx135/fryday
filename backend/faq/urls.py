from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, FAQTranslationViewSet

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)
router.register(r'faq-translations', FAQTranslationViewSet)

urlpatterns = router.urls