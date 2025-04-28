from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    # mi modelo de usuarios personalizado en el cual el campo user seria el email
    
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)

    REQUIRED_FIELDS = ('username',)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
    

    