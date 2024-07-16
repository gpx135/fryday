from rest_framework import viewsets
from .models import Feedback, ExternalReview
from .serializers import FeedbackSerializer, ExternalReviewSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ExternalReviewViewSet(viewsets.ModelViewSet):
    queryset = ExternalReview.objects.all()
    serializer_class = ExternalReviewSerializer