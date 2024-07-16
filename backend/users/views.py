from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    User, UserThirdPartyLogin, UserGroup, UserGroupMembership, UserDietaryPreference
)
from .serializers import (
    UserSerializer, UserThirdPartyLoginSerializer, UserGroupSerializer,
    UserGroupMembershipSerializer, UserDietaryPreferenceSerializer
)


class BaseViewSet(viewsets.ModelViewSet):
    """Base viewset that includes common behavior."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UserViewSet(BaseViewSet):
    """Viewset for managing Users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def third_party_logins(self, request, pk=None):
        """Custom action to get third-party logins for a user."""
        user = self.get_object()
        third_party_logins = UserThirdPartyLogin.objects.filter(user=user)
        serializer = UserThirdPartyLoginSerializer(third_party_logins, many=True)
        return Response(serializer.data)


class UserThirdPartyLoginViewSet(BaseViewSet):
    """Viewset for managing User Third-Party Logins."""
    queryset = UserThirdPartyLogin.objects.select_related('user')
    serializer_class = UserThirdPartyLoginSerializer


class UserGroupViewSet(BaseViewSet):
    """Viewset for managing User Groups."""
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


class UserGroupMembershipViewSet(BaseViewSet):
    """Viewset for managing User Group Memberships."""
    queryset = UserGroupMembership.objects.select_related('user', 'user_group')
    serializer_class = UserGroupMembershipSerializer


class UserDietaryPreferenceViewSet(BaseViewSet):
    """Viewset for managing User Dietary Preferences."""
    queryset = UserDietaryPreference.objects.select_related('user', 'dietary_preference')
    serializer_class = UserDietaryPreferenceSerializer
