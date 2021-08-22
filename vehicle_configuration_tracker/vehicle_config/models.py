from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


# Create your models here.

class Vehicle(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) #null=true temp
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)

    #dont need fields for these as they can be accesses by object.setup_set.all() ### add _set.all() at the end to get childs

    #assemblies = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    # assemblies = models.ManyToManyField('Assembly', null=True, blank=True) 
    # setups = models.ManyToManyField('Setup', null=True, blank=True)

    def __str__(self):
        return self.name

class Assembly(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100) 
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    parent_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=False) ## one to many

    # parts = models.ManyToManyField('Part', blank=True)
    assemblies = models.ManyToManyField("self", symmetrical=False)
    #is subassembly bool
    isSubassembly = models.BooleanField()
    

    class Meta:
        verbose_name = _('Assembly')
        verbose_name_plural = _('Assemblies')

class Setup(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    parent_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=False) #one to many
    # setup_params = models.ManyToManyField('SetupParam', blank=True)

    

class Part(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100) 
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)
    parent_assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, null=True, blank=False) #one to many, parent_assembly required as null=false by default

    def __str__(self):
        return self.name


    

class SetupParam(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100) 
    description = models.TextField()
    date_modifed = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(default=datetime.now)

    parts = models.ManyToManyField('Part', blank=True) # ??
    assemblies = models.ManyToManyField('Assembly', blank=True) # ??

    value = models.FloatField()
    parent_setup = models.ForeignKey(Setup, on_delete=models.CASCADE, null=True, blank=False) #one to many




    



    



