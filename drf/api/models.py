from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    reg_date = models.DateField()

class customer2(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    @property
    def is_authenticated(self):
        return True



