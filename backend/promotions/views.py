from rest_framework import viewsets
from .models import Promotion, PromotionTranslation, GiftCard
from .serializers import PromotionSerializer, PromotionTranslationSerializer, GiftCardSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class PromotionTranslationViewSet(viewsets.ModelViewSet):
    queryset = PromotionTranslation.objects.all()
    serializer_class = PromotionTranslationSerializer

class GiftCardViewSet(viewsets.ModelViewSet):
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer