from django.shortcuts import render
from datetime import datetime
from .models import Vehicle, Setup, Part, Assembly, SetupParam
import json
from django.core import serializers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    vehicles = Vehicle.objects.all()
    setups = Setup.objects.all()
    setup_params = SetupParam.objects.all()


    #setups = serializers.serialize("json",setups)
    context = {
        'vehicles' : vehicles,
        'setups' : setups,
        'setup_params' : setup_params

        #'setups' : json.dumps(setups)
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
    'setups' : Setup.objects.all(),
    'parts' : Part.objects.all(),
    'setups' : Setup.objects.all(),
    'setup_params' : SetupParam.objects.all(),
    }

    return render(request, 'vehicle_config/view.html', context)


# class PartListView(ListView):
#     model = Part
#     template_name = 'vehicle_config/view.html'
#     context_object_name = 'parts'
#     ordering = ['id']





def createPart(request): 
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        Part.objects.create(name=name, description=description)
        #id = Setup.objects.filter(description=description).values('id')[0]['id']
        msg = "successfully created part"
        return render(request, 'vehicle_config/createPart.html', {'msg':msg})

    context = {}
    return render(request, 'vehicle_config/createPart.html', context)

def editPart(request, pk): 
    part = get_object_or_404(Part, id=pk)
    if request.method == 'POST':
        

        name = request.POST['name']
        description = request.POST['description']
        Part.objects.filter(pk=part.id).update(name=name, description=description)

        msg = "successfully edited part"
        context = {
            'vehicles' : Vehicle.objects.all(),
            'setups' : Setup.objects.all(),
            'parts' : Part.objects.all(),
            'setups' : Setup.objects.all(),
            'setup_params' : SetupParam.objects.all(),
            }


        return render(request, 'vehicle_config/view.html', context)
        
        
    context = {'id': part.id, 'name': part.name, 'description': part.description}
    return render(request, 'vehicle_config/editPart.html', context)

def deletePart(request, pk):
    part = get_object_or_404(Part, id=pk)
    if request.method == 'POST':
        part.delete()
        context = {
            'vehicles' : Vehicle.objects.all(),
            'setups' : Setup.objects.all(),
            'parts' : Part.objects.all(),
            'setups' : Setup.objects.all(),
            'setup_params' : SetupParam.objects.all(),
            }
        return render(request, 'vehicle_config/view.html', context)
    context = {'id': part.id, 'name': part.name, 'description': part.description}
    return render(request, 'vehicle_config/deletePart.html', context)

        


def createSetup(request): 
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        car = request.POST['car']
        setup_params = request.POST['setup_params']

        #Setup.objects.create(description=description, car=car)

        if setup_params == "":
            s1 = Setup(name=name, car=car, description=description)
            s1.save()
            msg = "Successfully Created Setup"
        else:
            setup_params = setup_params.split(', ')
            for sp in setup_params:
                if SetupParam.objects.filter(name=sp).exists() == False:
                    msg = "The following setup parameter does not exist, please retry: " + "'" + sp + "'"
                    return render(request, 'vehicle_config/createSetup.html', {'msg':msg})

            s1 = Setup(name=name, car=car, description=description)
            s1.save()
            for sp in setup_params:
                sp1 = SetupParam.objects.filter(name=sp).get()
                s1.setup_params.add(sp1)
                s1.save()
            msg = "Successfully Created Setup"
            
        return render(request, 'vehicle_config/createSetup.html', {'msg':msg})
    
    context = {
    'vehicles' : Vehicle.objects.all(),
    'setups' : Setup.objects.all(), 
    'st' : "car4"
    }
    return render(request, 'vehicle_config/createSetup.html', context)


def createVehicle(request): 
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        assemblies = request.POST['assemblies']
        setups = request.POST['setups']

        if assemblies == "" and setups == "":
            v1 = Vehicle(name=name, description=description)
            v1.save()
            msg = "Successfully Created Vehicle"
        else:
            if assemblies == "":
                setups = setups.split(", ")
                for s in setups:
                    if Setup.objects.filter(name=s).exists() == False:
                        msg = "The following setup does not exist, please retry: " + "'" + s + "'"
                        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
                v1 = Vehicle(name=name, description=description)
                v1.save()

                for s in setups:
                    s1 = Setup.objects.filter(name=s).get()
                    v1.setups.add(s1)
                    v1.save()
                msg = "Successfully Created Vehicle"
            elif setups == "":
                assemblies = assemblies.split(", ")
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
                v1 = Vehicle(name=name, description=description)
                v1.save()
                for a in assemblies:
                    a1 = Assembly.objects.filter(name=a).get()
                    v1.assemblies.add(a1)
                    v1.save()
                msg = "Successfully Created Vehicle"

            else:
                assemblies = assemblies.split(", ")
                setups = setups.split(", ")
                
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
                for s in setups:
                    if Setup.objects.filter(name=s).exists() == False:
                        msg = "The following setup does not exist, please retry: " + "'" + s + "'"
                        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
                
                v1 = Vehicle(name=name, description=description)
                v1.save()

                for s in setups:
                    s1 = Setup.objects.filter(name=s).get()
                    v1.setups.add(s1)
                    v1.save()
                    
                for a in assemblies:
                    a1 = Assembly.objects.filter(name=a).get()
                    v1.assemblies.add(a1)
                    v1.save()

                msg = "Successfully Created Vehicle"
        return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})



    context = {}
    return render(request, 'vehicle_config/createVehicle.html', context)


def createSetupParam(request): 
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        value = request.POST['value']
        assemblies = request.POST['assemblies']
        parts = request.POST['parts']
        

        if assemblies == "" and parts == "":
            sp1 = SetupParam(name=name, description=description, value=value)
            sp1.save()
            msg = "Successfully Created Setup Parameter"
        else:
            if assemblies == "":
                parts = parts.split(", ")
                for p in parts:
                    if Part.objects.filter(name=p).exists() == False:
                        msg = "The following part does not exist, please retry: " + "'" + p + "'"
                        return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
                sp1 = SetupParam(name=name, description=description, value=value)
                sp1.save()

                for p in parts:
                    p1 = Part.objects.filter(name=p).get()
                    sp1.setups.add(p1)
                    sp1.save()
                msg = "Successfully Created Setup Parameter"
            elif parts == "":
                assemblies = assemblies.split(", ")
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
                sp1 = SetupParam(name=name, description=description, value=value)
                sp1.save()
                for a in assemblies:
                    a1 = Assembly.objects.filter(name=a).get()
                    sp1.assemblies.add(a1)
                    sp1.save()
                msg = "Successfully Created Setup Parameter"

            else:
                assemblies = assemblies.split(", ")
                parts = parts.split(", ")
                
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
                for p in parts:
                    if Part.objects.filter(name=p).exists() == False:
                        msg = "The following part does not exist, please retry: " + "'" + p + "'"
                        return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
                
                sp1 = SetupParam(name=name, description=description, value=value)
                sp1.save()

                for p in parts:
                    p1 = Part.objects.filter(name=p).get()
                    sp1.setups.add(p1)
                    sp1.save()
                    
                for a in assemblies:
                    a1 = Assembly.objects.filter(name=a).get()
                    sp1.assemblies.add(a1)
                    sp1.save()

                msg = "Successfully Created Setup Parameter"
        
        return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
    context = {}
    return render(request, 'vehicle_config/createSetupParam.html', context)
    



def createAssembly(request): 
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        parts = request.POST['parts']
        assemblies = request.POST['assemblies']

        if assemblies == "" and parts == "":
            a1 = Assembly(name=name, description=description)
            a1.save()
            msg = "Successfully Created Assembly"
        else:
            if assemblies == "":
                parts = parts.split(", ")
                for p in parts:
                    if Part.objects.filter(name=p).exists() == False:
                        msg = "The following part does not exist, please retry: " + "'" + p + "'"
                        return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                a1 = Assembly(name=name, description=description)
                a1.save()

                for p in parts:
                    p1 = Part.objects.filter(name=p).get()
                    a1.setups.add(p1)
                    a1.save()
                msg = "Successfully Created Assembly"
            elif parts == "":
                assemblies = assemblies.split(", ")
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                a1 = Assembly(name=name, description=description)
                a1.save()
                for a in assemblies:
                    subAssembly = Assembly.objects.filter(name=a).get()
                    a1.assemblies.add(subAssembly)
                    a1.save()
                msg = "Successfully Created Assembly"

            else:
                assemblies = assemblies.split(", ")
                parts = parts.split(", ")
                
                for a in assemblies:
                    if Assembly.objects.filter(name=a).exists() == False:
                        msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
                        return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                for p in parts:
                    if Part.objects.filter(name=p).exists() == False:
                        msg = "The following part does not exist, please retry: " + "'" + p + "'"
                        return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                
                a1 = Assembly(name=name, description=description)
                a1.save()
                for p in parts:
                    p1 = Part.objects.filter(name=p).get()
                    a1.setups.add(p1)
                    a1.save()
                for a in assemblies:
                    subAssembly = Assembly.objects.filter(name=a).get()
                    a1.assemblies.add(subAssembly)
                    a1.save()
                msg = "Successfully Created Assembly"

        return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})

    context = {}
    return render(request, 'vehicle_config/createAssembly.html', context)
    






