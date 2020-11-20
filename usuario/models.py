from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    bancaria = models.CharField(max_length=10, null=True, blank=True)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    direccion = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username
        