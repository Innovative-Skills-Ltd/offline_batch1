from rest_framework import generics
from .models import customer
from .serializers import customerSerializer

# List all books / Create a book
class customerListCreateView(generics.ListCreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

# Retrieve / Update / Delete a single book
class customerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer
