from rest_framework import serializers
from .models import APIIntegration, SyncLog

class APIIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIIntegration
        fields = '__all__'

class SyncLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncLog
        fields = '__all__'