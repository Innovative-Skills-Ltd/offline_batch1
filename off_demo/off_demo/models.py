from django.db import models

class Customer1(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Created timestamp
    file = models.FileField(upload_to='customers/')

class Customer2(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)


