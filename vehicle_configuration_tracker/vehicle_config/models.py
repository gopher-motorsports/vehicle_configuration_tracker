from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.
class Setup(models.Model):
    description = models.CharField(max_length=100, blank=True)

class SetupParam(models.Model):
    name = models.CharField(max_length=100) # <SetupParamENUM> ?
    description = models.CharField(max_length=100, blank=True)

    

class Vehicle(models.Model):
    name = models.CharField(max_length=100) 
    description = models.CharField(max_length=100, blank=True)

class Assembly(models.Model):
    name = models.CharField(max_length=100) # <assemblyParamENUM> ?
    description = models.CharField(max_length=100, blank=True)

class Part(models.Model):
    name = models.CharField(max_length=100) # <partENUM> ?
    description = models.CharField(max_length=100, blank=True)

