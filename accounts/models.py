from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

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
        ('freelancer', 'freelancer'),
        ('cscientifique', 'cscientifique'),
        ('digital', 'digital'),
        )

    ORGANE_CHOICES = (
        ('TFM', 'TFM'),
        ('SENEWEB', 'SENEWEB'),
        ('autre', 'autre'),
        )

    TYPE_ORGANE_CHOICES = (
        ('TFM', 'TFM'),
        ('SENEWEB', 'SENEWEB'),
        ('autre', 'autre'),
        )
    
    
    id = models.AutoField(primary_key=True) 
    email = models.EmailField(_("email address"), unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    #profession = models.CharField(max_length=45, blank=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)
    profile_organe = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)
    organe = models.CharField(choices=ORGANE_CHOICES, max_length=255,blank=True, null=True) 
    type_organe = models.CharField(choices=TYPE_ORGANE_CHOICES, max_length=255,blank=True, null=True)        
    date_joined = models.DateTimeField(default=timezone.now)
    reset_code = models.CharField(max_length=6, blank=True, null=True) 
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups',  # Nom d'accessor inversé personnalisé pour les groupes
        related_query_name='customuser',
    )

    # Champ d'autorisations d'utilisateur avec un related_name personnalisé
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions',  # Nom d'accessor inversé personnalisé pour les autorisations d'utilisateur
        related_query_name='customuser',
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
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
    

class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)