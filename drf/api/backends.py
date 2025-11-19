from django.contrib.auth.backends import BaseBackend
from .models import customer2
from django.contrib.auth.hashers import check_password

class CustomerBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = customer2.objects.get(email=email)
        except customer2.DoesNotExist:
            return None

        if check_password(password, user.password):
            return user
        
        return None

    def get_user(self, user_id):
        try:
            return customer2.objects.get(pk=user_id)
        except customer2.DoesNotExist:
            return None
