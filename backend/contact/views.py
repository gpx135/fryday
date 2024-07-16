from rest_framework import viewsets
from .models import NewsletterContact, ContactFormSubmission
from .serializers import NewsletterContactSerializer, ContactFormSubmissionSerializer

class NewsletterContactViewSet(viewsets.ModelViewSet):
    queryset = NewsletterContact.objects.all()
    serializer_class = NewsletterContactSerializer

class ContactFormSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer