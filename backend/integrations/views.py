from rest_framework import viewsets
from .models import APIIntegration, SyncLog
from .serializers import APIIntegrationSerializer, SyncLogSerializer

class APIIntegrationViewSet(viewsets.ModelViewSet):
    queryset = APIIntegration.objects.all()
    serializer_class = APIIntegrationSerializer

class SyncLogViewSet(viewsets.ModelViewSet):
    queryset = SyncLog.objects.all()
    serializer_class = SyncLogSerializer