from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
import uuid

# Create your models here.

# class Profil(models.Model):
#     PROFILE_CHOICES = (
#         ('admin', 'admin'),
#         ('groupecentrale', 'groupecentrale'),
#         ('presse', 'presse'),
#         )

#     # id = models.AutoField(primary_key=True) 
#     profession = models.CharField(primary_key=True, max_length=45, blank=True)
#     telephone = models.CharField(max_length=45, blank=True, null=True)
#     profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profil')

#     def __str__(self) :
#         return str(self.profile)

class CustomUser(AbstractUser):
    PROFILE_CHOICES = (
        ('admin', 'admin'),
        ('groupecentrale', 'groupecentrale'),
        ('presse', 'presse'),
        ('cscientifique', 'cscientifique'),
        ('digital', 'digital'),
        )

    id = models.AutoField(primary_key=True) 
    email = models.EmailField(_("email address"), unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    #profession = models.CharField(max_length=45, blank=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)     
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    #objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
# class CustomUser(AbstractBaseUser, PermissionsMixin):
    # PROFILE_CHOICES = (
    #     ('admin', 'admin'),
    #     ('groupecentrale', 'groupecentrale'),
    #     ('presse', 'presse'),
    #     )

    # # id = models.AutoField(primary_key=True) 
    # profession = models.CharField(primary_key=True, max_length=45, blank=True)
    # telephone = models.CharField(max_length=45, blank=True, null=True)
    # profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)
    # email = models.EmailField(_("email address"), unique=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # date_joined = models.DateTimeField(default=timezone.now)
    # telephone = models.CharField(max_length=45, blank=True, null=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    # def __str__(self):
    #     return self.email