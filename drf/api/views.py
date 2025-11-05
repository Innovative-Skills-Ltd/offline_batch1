from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import customer
from .serializers import customerSerializer, customerSerializer2
from django.core.mail import send_mail
# Create your views here.

from django.conf import settings

class customerListCreateView(generics.ListCreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

class customerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer


class UserRegisterView(APIView):
    def post(self, request):
        serializer = customerSerializer2(data=request.data)
        print(request.data)
        if serializer.is_valid():
            
            serializer.save()

            email = serializer.validated_data['email']
            subject = "Welcome to Innovative Skills LTD 🎉"
            message = f"Hi {email},\n\nYour registration was successful!\n\nThank you for joining us."

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )

            return Response(
                    {
                        "message": "✅ Registration successful! Email sent successfully.",
                        "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                    {
                        "message": "invalid data",
                        "data": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
