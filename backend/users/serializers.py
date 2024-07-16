from rest_framework import serializers
from .models import (
    User, UserThirdPartyLogin, UserGroup, UserGroupMembership, UserDietaryPreference
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserThirdPartyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserThirdPartyLogin
        fields = '__all__'

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'

class UserGroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroupMembership
        fields = '__all__'

class UserDietaryPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDietaryPreference
        fields = '__all__'