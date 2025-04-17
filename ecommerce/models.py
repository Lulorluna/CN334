from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Customer(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 address = models.CharField(max_length=500, blank=True)
 province = models.CharField(max_length=100, blank=True)
 post_code = models.CharField(max_length=5, blank=True)
 tel = models.CharField(max_length=20, blank=True)
