from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Part(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    # parent assemblies

class Assembly(models.Model):
    name = models.CharField(max_length=100) # <assemblyParamENUM> ?
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    parts = models.ManyToManyField('Part', blank=True)

    class Meta:
        verbose_name = _('Assembly')
        verbose_name_plural = _('Assemblies')
    # sub assemblies
    # parent vehicle
    

class SetupParam(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    parts = models.ManyToManyField('Part', blank=True)
    assemblies = models.ManyToManyField('Assembly', blank=True)
    value = models.FloatField()
    # parent setup??



class Setup(models.Model):
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    car = models.CharField(max_length=100, blank=False)
    setup_params = models.ManyToManyField('SetupParam', blank=True)
    setups_params = ArrayField(models.CharField(max_length=200), null=True, blank=True) #uncomment once you use postgres



class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    assemblies = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    setups = models.ManyToManyField('Setup', blank=True)


    



