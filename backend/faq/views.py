from rest_framework import viewsets
from .models import FAQ, FAQTranslation
from .serializers import FAQSerializer, FAQTranslationSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQTranslationViewSet(viewsets.ModelViewSet):
    queryset = FAQTranslation.objects.all()
    serializer_class = FAQTranslationSerializer