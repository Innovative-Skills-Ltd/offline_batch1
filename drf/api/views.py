from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,  status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import customer
from .serializers import customerSerializer, customerSerializer2
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

from django.conf import settings

class customerListCreateView(generics.ListCreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

class customerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserRegisterView(APIView):
    authentication_classes = []
    def post(self, request):

        serializer = customerSerializer2(data=request.data) 
        print(request.data)
        if serializer.is_valid():
            
            serializer.save()

            email = serializer.validated_data['email']
            subject = "Welcome to Innovative Skills LTD 🎉"
            message = f"Hi {email},\n\nYour registration was successful!\n\nThank you for joining us."

            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [email],
            #     fail_silently=False
            # )

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

class LoginViewV2(APIView):
    authentication_classes = []
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # <-- session created
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid email or password"}, status=400)
            
        # return Response({"message": request.data.get('email')})

from django.contrib.auth import login, authenticate
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  # <-- session created
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid email or password"}, status=400)
from rest_framework.permissions import IsAuthenticated

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "email": user.email,
            "active": user.is_active,
        })
