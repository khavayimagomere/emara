from __future__ import unicode_literals

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Home(models.Model):
    #timestamp = models.DateTimeField(default=datetime.datetime.now)
    current_section = models.IntegerField()
    


class Sections(models.Model):
    current_section = models.IntegerField()
    
    
class Papers(models.Model):
    current_section = models.IntegerField()
    
class About(models.Model):
    services = models.CharField(max_length=80)
    current_section = models.IntegerField()
    
class Contact(models.Model):
    name = models.CharField(max_length=65)
    email = models.EmailField(max_length=70, blank=True)
    message = models.TextField()




"""class ContactForm(models.Model):
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 50)
    password_confirmation = models.CharField(max_length = 50)
    current_section = models.IntegerField()
    email = models.EmailField(max_length=60)
    
    def _str_(self):
        return self.username"""
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()  
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()    
        
        
        

