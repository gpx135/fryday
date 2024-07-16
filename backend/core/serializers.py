from rest_framework import serializers
from .models import OpeningHours, SpecialClosure

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class SpecialClosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialClosure
        fields = '__all__'