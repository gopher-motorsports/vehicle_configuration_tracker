from django.shortcuts import render
from datetime import datetime
from .models import Vehicle, Setup
import json
from django.core import serializers

# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    setups = Setup.objects.all()
    setups = serializers.serialize("json",setups)
    context = {
        'vehicles' : vehicles,
        'setups' : json.dumps(setups)
    }
    return render(request, 'vehicle_config/home.html', context)

