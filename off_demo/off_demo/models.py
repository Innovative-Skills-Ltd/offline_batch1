from django.db import models

class Customer1(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Created timestamp
    file = models.FileField(upload_to='customers/')

class Course(models.Model):
    name = models.CharField(max_length=200)   # Course name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    cus_id = models.ManyToManyField(Customer1, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Created timestamp

class Customer2(models.Model):
    name = models.CharField(max_length=100)        # Customer name
    email = models.EmailField(unique=True)         # Email
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone number (optional)
    created_at = models.DateTimeField(auto_now_add=True)


