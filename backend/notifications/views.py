from rest_framework import viewsets
from .models import EmailTemplate, EmailTemplateTranslation
from .serializers import EmailTemplateSerializer, EmailTemplateTranslationSerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer

class EmailTemplateTranslationViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplateTranslation.objects.all()
    serializer_class = EmailTemplateTranslationSerializer