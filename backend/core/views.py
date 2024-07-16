from rest_framework import viewsets
from .models import OpeningHours, SpecialClosure
from .serializers import OpeningHoursSerializer, SpecialClosureSerializer

class OpeningHoursViewSet(viewsets.ModelViewSet):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer

class SpecialClosureViewSet(viewsets.ModelViewSet):
    queryset = SpecialClosure.objects.all()
    serializer_class = SpecialClosureSerializer