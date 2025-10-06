from django.db import models

class Customer1(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Created timestamp
class Customer2(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)