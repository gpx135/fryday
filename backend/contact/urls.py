from rest_framework.routers import DefaultRouter
from .views import NewsletterContactViewSet, ContactFormSubmissionViewSet

router = DefaultRouter()
router.register(r'newsletter-contacts', NewsletterContactViewSet)
router.register(r'contact-form-submissions', ContactFormSubmissionViewSet)

urlpatterns = router.urls