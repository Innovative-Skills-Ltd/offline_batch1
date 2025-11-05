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


