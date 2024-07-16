from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserThirdPartyLoginViewSet, UserGroupViewSet,
    UserGroupMembershipViewSet, UserDietaryPreferenceViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-third-party-logins', UserThirdPartyLoginViewSet)
router.register(r'user-groups', UserGroupViewSet)
router.register(r'user-group-memberships', UserGroupMembershipViewSet)
router.register(r'user-dietary-preferences', UserDietaryPreferenceViewSet)

urlpatterns = router.urls