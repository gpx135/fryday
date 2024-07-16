from rest_framework import viewsets
from .models import BuffetPricing, SpecialGroupPricing
from .serializers import BuffetPricingSerializer, SpecialGroupPricingSerializer

class BuffetPricingViewSet(viewsets.ModelViewSet):
    queryset = BuffetPricing.objects.all()
    serializer_class = BuffetPricingSerializer

class SpecialGroupPricingViewSet(viewsets.ModelViewSet):
    queryset = SpecialGroupPricing.objects.all()
    serializer_class = SpecialGroupPricingSerializer