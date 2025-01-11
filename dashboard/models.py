from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from accounts.models import *
from accounts.models import CustomUser
import uuid

# Create your models here.

class BanqueImange(models.Model):
    id = models.AutoField(primary_key=True) 
    events = models.CharField(max_length=255)
    comments = models.CharField(max_length=255, blank=True)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False, null=True , blank=True)
    publie = models.BooleanField(default=False, null=True , blank=True)
    statut = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, related_name='image')

    def __str__(self):
        return self.events
    
class BanqueImangePhoto(models.Model):
    id = models.AutoField(primary_key=True) 
    eventss = models.CharField(max_length=255)
    commentss = models.CharField(max_length=255, blank=True)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d/')
    publie = models.BooleanField(default=False, null=True , blank=True)
    statut = models.TextField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, related_name='imageadd')

    def __str__(self):
        return self.events

    
class BanqueRessource(models.Model):
    id = models.AutoField(primary_key=True) 
    eventsss = models.CharField(max_length=255)
    commentsss = models.CharField(max_length=255, blank=True)
    photo = models.FileField( upload_to='photos/%Y/%m/%d/')
    publie = models.BooleanField(default=False, null=True , blank=True)
    created_date = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, related_name='imageres')

    def __str__(self):
        return self.events

class Blog(models.Model):
    id = models.AutoField(primary_key=True) 
    tittle = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255, blank=True)
    photo = models.ImageField( upload_to='photos/%Y/%m/%d/')
    text = RichTextField(default=False, null=True , blank=True)
    statut = models.TextField(blank=True, null=True)
    is_featured = models.BooleanField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tittle



class Demande(models.Model):
    id = models.AutoField(primary_key=True) 
    nom = models.CharField(max_length=255)
    comments = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    adresse = models.CharField(max_length=255, null=True )
    telephone = models.CharField(max_length=255, blank=True)
    nbre = models.IntegerField(blank=True)
    pearson = models.CharField(max_length=255, blank=True)
    responsable = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False, null=True , blank=True)
    publie = models.BooleanField(default=False, null=True , blank=True)
    statut = models.TextField(blank=True, null=True)
    link_intagram = models.CharField(max_length=255, blank=True, null=True)
    link_website = models.CharField(max_length=255, blank=True, null=True)
    link_tiktok = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    #personnes = models.ManyToManyField(Personne)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='demandes')
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, related_name='demende')
    #profil = models.OneToOneField(Profil, on_delete=models.CASCADE, null=True, related_name='profil_demande')
 

class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE) 