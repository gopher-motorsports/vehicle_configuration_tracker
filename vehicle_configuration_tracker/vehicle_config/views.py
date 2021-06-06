from django.shortcuts import render
from datetime import datetime
from .models import Vehicle, Setup, Part, Assembly, SetupParam
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


def view(request):
    # vehicles = Vehicle.objects.all()
    # vehicles = serializers.serialize("json",vehicles)
    # setups = Setup.objects.all()
    # setups = serializers.serialize("json",setups)
    # context = {
    #     'vehicles' : json.dumps(vehicles),
    #     'setups' : json.dumps(setups)
    # }
    context = {
    'vehicles' : Vehicle.objects.all(),
    'setups' : Setup.objects.all()
    }
    

    
        

    return render(request, 'vehicle_config/view.html', context)

def createVehicle(request): 
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        assemblies = request.POST['assemblies']
        setups = request.POST['setups']

        context = {
            'name' : name,
            'description' : description,
            'assemblies' : assemblies,
            'setups' : setups,
        }

        if Vehicle.objects.filter(name=name).exists():
            msg = "car exists"
        else:
            v1 = Vehicle(name=name, description=description, assemblies=assemblies, setups=setups)
            v1.save()  
            #Vehicle.objects.create(name=name, description=description, assemblies=assemblies, setups=setups)
            msg = "successfull added vehicle"
        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})

    context = {}
    return render(request, 'vehicle_config/createVehicle.html', context)

def createSetup(request): 
    if request.method == 'POST':
        description = request.POST['description']
        car = request.POST['car']
        setup_params = request.POST['setup_params']

        context = {
            'description' : description,
            'car' : car,
            'setup_params' : setup_params,
        }
        
        Setup.objects.create(description=description, car=car, setup_params=setup_params)
        id = Setup.objects.filter(description=description).values('id')[0]['id']
        msg = "successfully created setup with id: " + str(id)

        return render(request, 'vehicle_config/createSetup.html', {'msg':msg})

    context = {}
    return render(request, 'vehicle_config/createSetup.html', context)
    





