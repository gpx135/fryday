from rest_framework.routers import DefaultRouter
from .views import EmailTemplateViewSet, EmailTemplateTranslationViewSet

router = DefaultRouter()
router.register(r'email-templates', EmailTemplateViewSet)
router.register(r'email-template-translations', EmailTemplateTranslationViewSet)

urlpatterns = router.urls