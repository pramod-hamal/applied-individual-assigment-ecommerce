from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = "CU", "Customer"
        VENDOR = "VE", "Vendor"
        ADMIN = "AD", "Admin"

    base_role = Role.CUSTOMER
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    role = models.CharField(max_length=3, choices=Role.choices, default=base_role)
