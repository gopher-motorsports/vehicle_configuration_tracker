from django.shortcuts import render, redirect
from datetime import datetime

## errors out?? 
#from vehicle_configuration_tracker.vehicle_config.apps import VehicleConfigConfig




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
    vehicles = Vehicle.objects.all().order_by('-date_created')
   

    
    # vehicles = Vehicle.objects.all()
    # vehicles = serializers.serialize("json",vehicles)
    # setups = Setup.objects.all()
    # setups = serializers.serialize("json",setups)
    # context = {
    #     'vehicles' : json.dumps(vehicles),
    #     'setups' : json.dumps(setups)
    # }
    context = {

    'vehicles' : vehicles,
    }

    return render(request, 'vehicle_config/view.html', context)


# class PartListView(ListView):
#     model = Part
#     template_name = 'vehicle_config/view.html'
#     context_object_name = 'parts'
#     ordering = ['id']

def viewVehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, id=pk)

    if request.method == 'POST':
        obj = "Vehicle"
        context = {
        'id': vehicle.id, 
        'name': vehicle.name,
        'description': vehicle.description,
        'obj': obj,
        'assemblies': vehicle.assembly_set.all().filter(isSubassembly=False).order_by('-date_created'),
        'setups': vehicle.setup_set.all().order_by('-date_created')
    }
        return render(request, 'vehicle_config/createVehicle.html', context)
    # vAssemblies = vehicle.assemblies
    # vSetups = vehicle.setups
    obj = "Vehicle"
    context = {
        'id': vehicle.id, 
        'name': vehicle.name,
        'description': vehicle.description,
        'obj': obj,
        'vehicle': vehicle,
        'assemblies': vehicle.assembly_set.all().filter(isSubassembly=False).order_by('-date_created'),
        'setups': vehicle.setup_set.all().order_by('-date_created')
    }
    return render(request, 'vehicle_config/viewVehicle.html', context)

# def viewSetup(request, pk):
#     setup = get_object_or_404(Setup, id=pk)
#     obj = "Setup"
#     setup_params = setup.setupparam_set.all().order_by('-date_created')
#     if request.method == 'POST':
#         context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
#         return render(request, 'vehicle_config/viewSetup.html', context)
    
    
#     context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
#     return render(request, 'vehicle_config/viewSetup.html', context)


def viewSetup(request, pk):
    setup = get_object_or_404(Setup, id=pk)
    obj = "Setup"
    setup_params = setup.setupparam_set.all().order_by('-date_created')
    if request.method == 'POST':
        context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
        return render(request, 'vehicle_config/viewSetup.html', context)
    
    
    context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
    return render(request, 'vehicle_config/viewSetup.html', context)

def viewSetup2(request, pk):
    setup = get_object_or_404(Setup, id=pk)
    obj = "Setup"
    setup_params = setup.setupparam_set.all()

    # General Information
    event_name = setup_params.filter(name="Event Name").get()
    driver_name = setup_params.filter(name="Driver Name").get()
    track = setup_params.filter(name="Track").get()
    #date = request.POST['date']
    ambient_temp = setup_params.filter(name="Ambient Temperature").get()
    track_temp = setup_params.filter(name="Track Temperature").get()

    # Front, Left Side
    cold_pressure_fl =setup_params.filter(name="Cold Pressure - Front Left Tire").get()
    hot_pressure_fl = setup_params.filter(name="Hot Pressure - Front Left Tire").get()
    camber_fl = setup_params.filter(name="Camber - Front Left").get()
    toe_fl = setup_params.filter(name="Toe - Front Left").get()
    ls_compression_fl = setup_params.filter(name="LS Compression - Front Left").get()
    hs_compression_fl = setup_params.filter(name="HS Compression - Front Left").get()
    hs_rebound_fl = setup_params.filter(name="HS Rebound - Front Left").get()

    # Front, Right Side
    cold_pressure_fr = setup_params.filter(name="Cold Pressure - Front Right Tire").get()
    hot_pressure_fr = setup_params.filter(name="Hot Pressure - Front Right Tire").get()
    camber_fr = setup_params.filter(name="Camber - Front Right").get()
    toe_fr = setup_params.filter(name="Toe - Front Right").get()
    ls_compression_fr = setup_params.filter(name="LS Compression - Front Right").get()
    hs_compression_fr = setup_params.filter(name="HS Compression - Front Right").get()
    hs_rebound_fr = setup_params.filter(name="HS Rebound - Front Right").get()


    # Front, Center
    ride_height_f = setup_params.filter(name="Ride Height - Front").get()
    wing_f = setup_params.filter(name="Wing - Front").get()
    spring_rate_f = setup_params.filter(name="Spring Rate - Front").get()
    arb_setting_f = setup_params.filter(name="ARB Setting - Front").get()

    # Back, Left Side
    cold_pressure_bl = setup_params.filter(name="Cold Pressure - Back Left Tire").get()
    hot_pressure_bl = setup_params.filter(name="Hot Pressure - Back Left Tire").get()
    camber_bl = setup_params.filter(name="Camber - Back Left").get()
    toe_bl = setup_params.filter(name="Toe - Back Left").get()
    ls_compression_bl = setup_params.filter(name="LS Compression - Back Left").get()
    hs_compression_bl = setup_params.filter(name="HS Compression - Back Left").get()
    hs_rebound_bl = setup_params.filter(name="HS Rebound - Back Left").get()


    # Back, Right Side
    cold_pressure_br = setup_params.filter(name="Cold Pressure - Back Right Tire").get()
    hot_pressure_br = setup_params.filter(name="Hot Pressure - Back Right Tire").get()
    camber_br = setup_params.filter(name="Camber - Back Right").get()
    toe_br = setup_params.filter(name="Toe - Back Right").get()
    ls_compression_br = setup_params.filter(name="LS Compression - Back Right").get()
    hs_compression_br = setup_params.filter(name="HS Compression - Back Right").get()
    hs_rebound_br = setup_params.filter(name="HS Rebound - Back Right").get()


    # Back, Center
    ride_height_b = setup_params.filter(name="Ride Height - Back").get()
    wing_b = setup_params.filter(name="Wing - Back").get()
    spring_rate_b = setup_params.filter(name="Spring Rate - Back").get()
    arb_setting_b = setup_params.filter(name="ARB Setting - Back").get()

    # Adj Info for Shocks
    shock_info = setup_params.filter(name="Shocks Information").get()
    
    # Team Notes / Track Info
    team_notes = setup_params.filter(name="Team Notes").get()
    track_info = setup_params.filter(name="Track Information").get()

    # Driver Feedback
    driver_feedback = setup_params.filter(name="Driver Feedback").get()

    if request.method == 'POST':
    
        # General Information
        event_name = request.POST['event-name']
        driver_name = request.POST['driver-name']
        track = request.POST['track']
        #date = request.POST['date']
        ambient_temp = request.POST['ambient-temp']
        track_temp = request.POST['track-temp']

        # Front, Left Side
        cold_pressure_fl = request.POST['cold-pressure-fl']
        hot_pressure_fl = request.POST['hot-pressure-fl']
        camber_fl = request.POST['camber-fl']
        toe_fl = request.POST['toe-fl']
        ls_compression_fl = request.POST['ls-compression-fl']
        hs_compression_fl = request.POST['hs-compression-fl']
        hs_rebound_fl = request.POST['hs-rebound-fl']

        # Front, Right Side
        cold_pressure_fr = request.POST['cold-pressure-fr']
        hot_pressure_fr = request.POST['hot-pressure-fr']
        camber_fr = request.POST['camber-fr']
        toe_fr = request.POST['toe-fr']
        ls_compression_fr = request.POST['ls-compression-fr']
        hs_compression_fr = request.POST['hs-compression-fr']
        hs_rebound_fr = request.POST['hs-rebound-fr']

        # Front, Center
        ride_height_f = request.POST['ride-height-f']
        wing_f = request.POST['wing-f']
        spring_rate_f = request.POST['spring-rate-f']
        arb_setting_f = request.POST['arb-setting-f']

        # Back, Left Side
        cold_pressure_bl = request.POST['cold-pressure-bl']
        hot_pressure_bl = request.POST['hot-pressure-bl']
        camber_bl = request.POST['camber-bl']
        toe_bl = request.POST['toe-bl']
        ls_compression_bl = request.POST['ls-compression-bl']
        hs_compression_bl = request.POST['hs-compression-bl']
        hs_rebound_bl = request.POST['hs-rebound-bl']

        # Back, Right Side
        cold_pressure_br = request.POST['cold-pressure-br']
        hot_pressure_br = request.POST['hot-pressure-br']
        camber_br = request.POST['camber-br']
        toe_br = request.POST['toe-br']
        ls_compression_br = request.POST['ls-compression-br']
        hs_compression_br = request.POST['hs-compression-br']
        hs_rebound_br = request.POST['hs-rebound-br']

        # Back, Center
        ride_height_b = request.POST['ride-height-b']
        wing_b = request.POST['wing-b']
        spring_rate_b = request.POST['spring-rate-b']
        arb_setting_b = request.POST['arb-setting-b']

        # Adj Info for Shocks
        shock_info = request.POST['shock-info']
        
        # Team Notes / Track Info
        team_notes = request.POST['team-notes']
        track_info = request.POST['track-info']

        # Driver Feedback
        driver_feedback = request.POST['driver-feedback']

        # updating values
        setup_params.filter(name="Event Name").update(value=event_name)
        setup_params.filter(name="Driver Name").update(value=driver_name)
        setup_params.filter(name="Track").update(value=track)
        setup_params.filter(name="Ambient Temperature").update(value=ambient_temp )
        setup_params.filter(name="Track Temperature").update(value=track_temp)

        # Front, Left Side
        setup_params.filter(name="Cold Pressure - Front Left Tire").update(value=cold_pressure_fl)
        setup_params.filter(name="Hot Pressure - Front Left Tire").update(value=hot_pressure_fl )
        setup_params.filter(name="Camber - Front Left").update(value=camber_fl)
        setup_params.filter(name="Toe - Front Left").update(value=toe_fl)
        setup_params.filter(name="LS Compression - Front Left").update(value=ls_compression_fl)
        setup_params.filter(name="HS Compression - Front Left").update(value=hs_compression_fl)
        setup_params.filter(name="HS Rebound - Front Left").update(value=hs_rebound_fl)

        # Front, Right Side
        setup_params.filter(name="Cold Pressure - Front Right Tire").update(value=cold_pressure_fr)
        setup_params.filter(name="Hot Pressure - Front Right Tire").update(value=hot_pressure_fr )
        setup_params.filter(name="Camber - Front Right").update(value=camber_fr)
        setup_params.filter(name="Toe - Front Right").update(value=toe_fr)
        setup_params.filter(name="LS Compression - Front Right").update(value=ls_compression_fr)
        setup_params.filter(name="HS Compression - Front Right").update(value=hs_compression_fr)
        setup_params.filter(name="HS Rebound - Front Right").update(value=hs_rebound_fr)


        # Front, Center
        setup_params.filter(name="Ride Height - Front").update(value=ride_height_f)
        setup_params.filter(name="Wing - Front").update(value=wing_f)
        setup_params.filter(name="Spring Rate - Front").update(value=spring_rate_f)
        setup_params.filter(name="ARB Setting - Front").udpate(value=arb_setting_f)

        # Back, Left Side
        setup_params.filter(name="Cold Pressure - Back Left Tire").update(value=cold_pressure_bl)
        setup_params.filter(name="Hot Pressure - Back Left Tire").update(value=hot_pressure_bl)
        setup_params.filter(name="Camber - Back Left").update(value=camber_bl)
        setup_params.filter(name="Toe - Back Left").update(value=toe_bl)
        setup_params.filter(name="LS Compression - Back Left").update(value=ls_compression_bl)
        setup_params.filter(name="HS Compression - Back Left").update(value=hs_compression_bl)
        setup_params.filter(name="HS Rebound - Back Left").update(value=hs_rebound_bl)


        # Back, Right Side
        setup_params.filter(name="Cold Pressure - Back Right Tire").update(value=cold_pressure_br)
        setup_params.filter(name="Hot Pressure - Back Right Tire").update(value=hot_pressure_br)
        setup_params.filter(name="Camber - Back Right").update(value=camber_br)
        setup_params.filter(name="Toe - Back Right").update(value=toe_br)
        setup_params.filter(name="LS Compression - Back Right").update(value=ls_compression_br)
        setup_params.filter(name="HS Compression - Back Right").update(value=hs_compression_br)
        setup_params.filter(name="HS Rebound - Back Right").update(value=hs_rebound_br)


        # Back, Center
        setup_params.filter(name="Ride Height - Back").update(value=ride_height_b)
        setup_params.filter(name="Wing - Back").update(value=wing_b)
        setup_params.filter(name="Spring Rate - Back").update(value=spring_rate_b)
        setup_params.filter(name="ARB Setting - Back").update(value=arb_setting_b)

        # Adj Info for Shocks
        setup_params.filter(name="Shocks Information").update(value=shock_info)
        
        # Team Notes / Track Info
        setup_params.filter(name="Team Notes").update(value=team_notes)
        setup_params.filter(name="Track Information").update(value=track_info)

        # Driver Feedback
        setup_params.filter(name="Driver Feedback").update(value=driver_feedback)
       
        return redirect("success", obj="Setup", pk=pk)
    
    
    context = {'id': setup.id, 'setup':setup, 'obj':obj, 
    'event_name':event_name, 'driver_name':driver_name, 'track':track, 'ambient_temp':ambient_temp, 'track_temp':track_temp,
    'cold_pressure_fl':cold_pressure_fl, 'hot_pressure_fl':hot_pressure_fl, 'camber_fl':camber_fl, 'toe_fl':toe_fl, 'ls_compression_fl':ls_compression_fl, 'hs_compression_fl':hs_compression_fl, 'hs_rebound_fl':hs_rebound_fl,
    'cold_pressure_fr':cold_pressure_fr, 'hot_pressure_fr':hot_pressure_fr, 'camber_fr':camber_fr, 'toe_fr':toe_fr, 'ls_compression_fr':ls_compression_fr, 'hs_compression_fr':hs_compression_fr, 'hs_rebound_fr':hs_rebound_fr,
    'ride_height_f':ride_height_f, 'wing_f':wing_f, 'spring_rate_f':spring_rate_f, 'arb_setting_f':arb_setting_f,
    'cold_pressure_br':cold_pressure_br, 'hot_pressure_br':hot_pressure_br, 'camber_br':camber_br, 'toe_br':toe_br, 'ls_compression_br':ls_compression_br, 'hs_compression_br':hs_compression_br, 'hs_rebound_br':hs_rebound_br,
    'cold_pressure_bl':cold_pressure_bl, 'hot_pressure_bl':hot_pressure_bl, 'camber_bl':camber_bl, 'toe_bl':toe_bl, 'ls_compression_bl':ls_compression_bl, 'hs_compression_bl':hs_compression_bl, 'hs_rebound_bl':hs_rebound_bl,
    'ride_height_b':ride_height_b, 'wing_b':wing_b, 'spring_rate_b':spring_rate_b, 'arb_setting_b':arb_setting_b,
    'shock_info':shock_info,
    'team_notes':team_notes, 'track_info':track_info,
    'driver_feedback':driver_feedback }
   
    return render(request, 'vehicle_config/viewSetup2.html', context)


def viewAssembly(request, pk):
    assembly = get_object_or_404(Assembly, id=pk)
    sub_assemblies = assembly.assemblies.all().order_by('-date_created')
    obj = "Assembly"
    
    #parent_vehicle_id = assembly.parent_vehicle
    parts = assembly.part_set.all().order_by('-date_created')
    if assembly.isSubassembly:
        parent_assembly = assembly.parentAssembly.all()[0]
    else:
        parent_assembly = None
    if request.method == 'POST':
        context = {'id': assembly.id, 'assembly':assembly, 'obj':obj, 'parts':parts, 'sub_assemblies':sub_assemblies, 'parent_assembly':parent_assembly}
        return render(request, 'vehicle_config/viewAssembly.html', context)

    if assembly.setupparam_set.all().first():
        setupParams = assembly.setupparam_set.all()
        spex = True
    else:
        setupParams = "None"
        spex = False
    
    
    context = {'id': assembly.id, 'assembly':assembly, 'obj':obj, 'parts':parts, 'sub_assemblies':sub_assemblies, 'parent_assembly':parent_assembly, 'setupParams':setupParams, 'spex':spex}
    return render(request, 'vehicle_config/viewAssembly.html', context)


def viewPart(request, pk):
    part = get_object_or_404(Part, id=pk)
    obj = "Part"
    parent_assembly = part.parent_assembly
    if part.setupparam_set.all().first():
        setupParams = part.setupparam_set.all()
        spex = True
    else:
        setupParams = "None"
        spex = False


    #parent_vehicle_id = assembly.parent_ve
    if request.method == 'POST':
        context = {'id': part.id, 'name':part.name, 'obj':obj, 'part':part, 'parent_assembly':parent_assembly, 'setupParams':setupParams, 'spex':spex}
        return render(request, 'vehicle_config/viewPart.html', context)
    
    
    context = {'id': part.id, 'name':part.name, 'obj':obj, 'part':part, 'parent_assembly':parent_assembly, 'setupParams':setupParams, 'spex':spex}
    return render(request, 'vehicle_config/viewPart.html', context)

def formTest(request, pk):
    setup = get_object_or_404(Setup, id=pk)
    context = {'id:', setup.id}
    return render(request, 'vehicle_config/formTest.html', context)

def viewSetupParam(request, pk):
    setupParam = get_object_or_404(SetupParam, id=pk)
 
    obj = "SetupParam"
    
    #parent_vehicle_id = assembly.parent_vehicle
    parts = setupParam.parts.all().order_by('name') 
    assemblies = setupParam.assemblies.all().order_by('name') 
    parent_setup = setupParam.parent_setup
    add = "add"
    rem = "rem"

    allParts = Part.objects.none() ## create empty queryset
    allPartsInt = Part.objects.all()
    for part in allPartsInt:
        if part.parent_assembly.parent_vehicle == parent_setup.parent_vehicle:
            if not setupParam.parts.filter(pk=part.pk).exists():
                allParts |= Part.objects.filter(pk=part.pk) ## this line was a buncha bs, adding part from particula vehicle to empty queryset

    allAssemblies = Assembly.objects.none()
    allAssembliesInt = Assembly.objects.all().filter(parent_vehicle=parent_setup.parent_vehicle).order_by('name') ## find all assemblies/parts for a particular vehicle and order alphabetically
    for assembly in allAssembliesInt:
        if not setupParam.assemblies.filter(pk=assembly.pk).exists():
            allAssemblies |= Assembly.objects.filter(pk=assembly.pk)

    

    if request.method == 'POST':
        context = {'id': setupParam.id, 'setupParam':setupParam, 'obj':obj, 'parts':parts, 'assemblies':assemblies, 'parent_setup':parent_setup, 'allParts':allParts, 'allAssemblies':allAssemblies, 'vehicle_name':parent_setup.parent_vehicle.name, 'add':add, 'rem':rem}
        return render(request, 'vehicle_config/viewSetupParam.html', context)
    
    
    context = {'id': setupParam.id, 'setupParam':setupParam, 'obj':obj, 'parts':parts, 'assemblies':assemblies, 'parent_setup':parent_setup, 'allParts':allParts, 'allAssemblies':allAssemblies,  'vehicle_name':parent_setup.parent_vehicle.name, 'add':add, 'rem':rem}
    return render(request, 'vehicle_config/viewSetupParam.html', context)

def spPart(request, spPk, pk, act):
    if act=="add":
        setupParam = get_object_or_404(SetupParam, id=spPk)
        part = get_object_or_404(Part, id=pk)
        setupParam.parts.add(part)
        setupParam.save()
        return redirect('viewSetupParam', pk=spPk)
    else:
        setupParam = get_object_or_404(SetupParam, id=spPk)
        part = get_object_or_404(Part, id=pk)
        setupParam.parts.remove(part)
        setupParam.save()
        return redirect('viewSetupParam', pk=spPk)


def spAssembly(request, spPk, pk, act):
    if act=="add":
        setupParam = get_object_or_404(SetupParam, id=spPk)
        assembly = get_object_or_404(Assembly, id=pk)
        setupParam.assemblies.add(assembly)
        setupParam.save()
        return redirect('viewSetupParam', pk=spPk)
    else:
        setupParam = get_object_or_404(SetupParam, id=spPk)
        assembly = get_object_or_404(Assembly, id=pk)
        setupParam.assemblies.remove(assembly)
        setupParam.save()
        return redirect('viewSetupParam', pk=spPk)


def success(request, obj, pk):
    actual_obj = get_object_or_404(eval(obj), id=pk)
    context = {'id':pk, 'obj':obj}

    if obj == "Vehicle":
        return redirect('viewVehicle', pk=pk)
    elif obj == "Setup":
        return redirect('viewSetup', pk=pk)
    elif obj == "Assembly":
        return redirect('viewAssembly', pk=pk)
    elif obj == "Part":
        return redirect('viewPart', pk=pk)
    elif obj == "SetupParam":
        return redirect('viewSetupParam', pk=pk)
  



def edit(request, obj, pk):
     
    actual_obj = get_object_or_404(eval(obj), id=pk)
    if request.method == 'POST': 
        name = request.POST['name']
        description = request.POST['description']

        eval(obj).objects.filter(pk=actual_obj.id).update(name=name, description=description)

        if obj=="Part":
            part_number = request.POST['part_number']
            eval(obj).objects.filter(pk=actual_obj.id).update(part_number=part_number)
        elif obj == "SetupParam":
            value = request.POST['value']
            units = request.POST['units']
            eval(obj).objects.filter(pk=actual_obj.id).update(value=value, units=units)


        msg = "ID: " + str(actual_obj.id) + ", Name: " + str(actual_obj.name)
        context = {
            'id':pk,
           'actual_obj':actual_obj,  
            'objType': obj,
            'msg' : msg
        }
        #view/edit/<str:obj>/<int:pk>/success
        #addr = "view/edit/" + obj + "/" + str(pk) + "/success" 
        return redirect("success/", obj=obj, pk=pk)
        #return render(request, 'vehicle_config/success.html', context)

    isPart = False
    isSetupParam = False
    if obj=="Part":
        isPart = True
    if obj=="SetupParam":
        isSetupParam = True
    
        
    context = {'id': actual_obj.id, 'obj': obj, 'name': actual_obj.name, 'description': actual_obj.description,'isPart': isPart, 'isSetupParam':isSetupParam, 'actual_obj':actual_obj}
    return render(request, 'vehicle_config/edit.html', context)


def delete(request, obj, pk):
    actual_obj = get_object_or_404(eval(obj), id=pk)
    if request.method == 'POST':
        if obj == "Vehicle":
            actual_obj.delete()
            return redirect('/view')
        elif obj == "Setup":
            parent_vehicle = actual_obj.parent_vehicle.id
            actual_obj.delete()
            return redirect('viewVehicle', pk=parent_vehicle)
        elif obj == "Assembly":
            parent_vehicle = actual_obj.parent_vehicle.id
            
            
            if actual_obj.isSubassembly:
                parent_assembly = actual_obj.parentAssembly.all()[0].id
                
                actual_obj.delete()
                return redirect('viewAssembly', pk=parent_assembly)
            else:
                actual_obj.delete()
                return redirect('viewVehicle', pk=parent_vehicle)
        elif obj == "Part":
            parent_assembly = actual_obj.parent_assembly.id
            actual_obj.delete()
            return redirect('viewAssembly', pk=parent_assembly)
        elif obj == "SetupParam":
            parent_setup = actual_obj.parent_setup.id
            actual_obj.delete()
            return redirect('viewSetup', pk=parent_setup)
            


    context = {'id': actual_obj.id, 'name': actual_obj.name, 'obj':obj}
    return render(request, 'vehicle_config/delete.html', context)

        


def createSetup(request, pk):
    parent_vehicle = get_object_or_404(Vehicle, id=pk)
    if request.method == 'POST':

        # General Information
        event_name = request.POST['event-name']
        driver_name = request.POST['driver-name']
        track = request.POST['track']
        #date = request.POST['date']
        ambient_temp = request.POST['ambient-temp']
        track_temp = request.POST['track-temp']

        # Front, Left Side
        cold_pressure_fl = request.POST['cold-pressure-fl']
        hot_pressure_fl = request.POST['hot-pressure-fl']
        camber_fl = request.POST['camber-fl']
        toe_fl = request.POST['toe-fl']
        ls_compression_fl = request.POST['ls-compression-fl']
        hs_compression_fl = request.POST['hs-compression-fl']
        hs_rebound_fl = request.POST['hs-rebound-fl']

        # Front, Right Side
        cold_pressure_fr = request.POST['cold-pressure-fr']
        hot_pressure_fr = request.POST['hot-pressure-fr']
        camber_fr = request.POST['camber-fr']
        toe_fr = request.POST['toe-fr']
        ls_compression_fr = request.POST['ls-compression-fr']
        hs_compression_fr = request.POST['hs-compression-fr']
        hs_rebound_fr = request.POST['hs-rebound-fr']

        # Front, Center
        ride_height_f = request.POST['ride-height-f']
        wing_f = request.POST['wing-f']
        spring_rate_f = request.POST['spring-rate-f']
        arb_setting_f = request.POST['arb-setting-f']

        # Back, Left Side
        cold_pressure_bl = request.POST['cold-pressure-bl']
        hot_pressure_bl = request.POST['hot-pressure-bl']
        camber_bl = request.POST['camber-bl']
        toe_bl = request.POST['toe-bl']
        ls_compression_bl = request.POST['ls-compression-bl']
        hs_compression_bl = request.POST['hs-compression-bl']
        hs_rebound_bl = request.POST['hs-rebound-bl']

        # Back, Right Side
        cold_pressure_br = request.POST['cold-pressure-br']
        hot_pressure_br = request.POST['hot-pressure-br']
        camber_br = request.POST['camber-br']
        toe_br = request.POST['toe-br']
        ls_compression_br = request.POST['ls-compression-br']
        hs_compression_br = request.POST['hs-compression-br']
        hs_rebound_br = request.POST['hs-rebound-br']

        # Back, Center
        ride_height_b = request.POST['ride-height-b']
        wing_b = request.POST['wing-b']
        spring_rate_b = request.POST['spring-rate-b']
        arb_setting_b = request.POST['arb-setting-b']

        # Adj Info for Shocks
        shock_info = request.POST['shock-info']
        
        # Team Notes / Track Info
        team_notes = request.POST['team-notes']
        track_info = request.POST['track-info']

        # Driver Feedback
        driver_feedback = request.POST['driver-feedback']

        # Create Setup Object
        curSetup = Setup.objects.create(name=event_name, parent_vehicle=parent_vehicle)
        curSetup.save()

        # General Information Setup Parameters
        SetupParam.objects.create(value=event_name, name="Event Name", parent_setup=curSetup)
        SetupParam.objects.create(value=driver_name, name="Driver Name", parent_setup=curSetup)
        SetupParam.objects.create(value=track, name="Track", parent_setup=curSetup)
        SetupParam.objects.create(value=ambient_temp, units="farenheit", name="Ambient Temperature", parent_setup=curSetup)
        SetupParam.objects.create(value=track_temp, units="farenheit", name="Track Temperature", parent_setup=curSetup)
        
        # Front, Left Side SetupParam Object Creation
        SetupParam.objects.create(value=cold_pressure_fl, units="psi", name="Cold Pressure - Front Left Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=hot_pressure_fl, units="psi", name="Hot Pressure - Front Left Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=camber_fl, units="deg", name="Camber - Front Left", parent_setup=curSetup)
        SetupParam.objects.create(value=toe_fl, units="deg", name="Toe - Front Left", parent_setup=curSetup)
        SetupParam.objects.create(value=ls_compression_fl, name="LS Compression - Front Left", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_compression_fl, name="HS Compression - Front Left", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_rebound_fl, name="HS Rebound - Front Left", parent_setup=curSetup)

        # Front, Right Side SetupParam Object Creation
        SetupParam.objects.create(value=cold_pressure_fr, units="psi", name="Cold Pressure - Front Right Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=hot_pressure_fr, units="psi", name="Hot Pressure - Front Right Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=camber_fr, units="deg", name="Camber - Front Right", parent_setup=curSetup)
        SetupParam.objects.create(value=toe_fr, units="deg", name="Toe - Front Right", parent_setup=curSetup)
        SetupParam.objects.create(value=ls_compression_fr, name="LS Compression - Front Right", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_compression_fr, name="HS Compression - Front Right", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_rebound_fr, name="HS Rebound - Front Right", parent_setup=curSetup)

        # Front, Center Object Creation
        SetupParam.objects.create(value=ride_height_f, name="Ride Height - Front", parent_setup=curSetup)
        SetupParam.objects.create(value=wing_f, name="Wing - Front", parent_setup=curSetup)
        SetupParam.objects.create(value=spring_rate_f, name="Spring Rate - Front", parent_setup=curSetup)
        SetupParam.objects.create(value=arb_setting_f, name="ARB Setting - Front", parent_setup=curSetup)
        
        # Back, Left Side SetupParam Object Creation
        SetupParam.objects.create(value=cold_pressure_bl, units="psi", name="Cold Pressure - Back Left Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=hot_pressure_bl, units="psi", name="Hot Pressure - Back Left Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=camber_bl, units="deg", name="Camber - Back Left", parent_setup=curSetup)
        SetupParam.objects.create(value=toe_bl, units="deg", name="Toe - Back Left", parent_setup=curSetup)
        SetupParam.objects.create(value=ls_compression_bl, name="LS Compression - Back Left", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_compression_bl, name="HS Compression - Back Left", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_rebound_bl, name="HS Rebound - Back Left", parent_setup=curSetup)
        
        
        # Back, Right Side SetupParam Object Creation
        SetupParam.objects.create(value=cold_pressure_br, units="psi", name="Cold Pressure - Back Right Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=hot_pressure_br, units="psi", name="Hot Pressure - Back Right Tire", parent_setup=curSetup)
        SetupParam.objects.create(value=camber_br, units="deg", name="Camber - Back Right", parent_setup=curSetup)
        SetupParam.objects.create(value=toe_br, units="deg", name="Toe - Back Right", parent_setup=curSetup)
        SetupParam.objects.create(value=ls_compression_br, name="LS Compression - Back Right", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_compression_br, name="HS Compression - Back Right", parent_setup=curSetup)
        SetupParam.objects.create(value=hs_rebound_br, name="HS Rebound - Back Right", parent_setup=curSetup)
        
        # Back, Center Object Creation
        SetupParam.objects.create(value=ride_height_b, name="Ride Height - Back", parent_setup=curSetup)
        SetupParam.objects.create(value=wing_b, name="Wing - Back", parent_setup=curSetup)
        SetupParam.objects.create(value=spring_rate_b, name="Spring Rate - Back", parent_setup=curSetup)
        SetupParam.objects.create(value=arb_setting_b, name="ARB Setting - Back", parent_setup=curSetup)

        # Shocks Info Object
        SetupParam.objects.create(description=shock_info, name="Shocks Information", parent_setup=curSetup)
        
        # Team Notes / Track Info Objs
        SetupParam.objects.create(description=team_notes, name="Team Notes", parent_setup=curSetup)
        SetupParam.objects.create(description=track_info, name="Track Information", parent_setup=curSetup)

        # Driver Feedback Obj
        SetupParam.objects.create(description=driver_feedback, name="Driver Feedback", parent_setup=curSetup)

        return redirect('viewVehicle', pk=pk)

    context = {'parent_vehicle':parent_vehicle}
    return render(request, 'vehicle_config/createSetup.html', context)

def createAssembly(request, pk, pid):
    parent_vehicle = get_object_or_404(Vehicle, id=pk)
    
    
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        
        #a1 = Assembly.objects.create(name=name, description=description, parent_vehicle=parent_vehicle)
        if pid != 0:
            a1 = Assembly(name=name, description=description, parent_vehicle=parent_vehicle, isSubassembly=True)
            a1.save()
            parent_assembly = get_object_or_404(Assembly, id=pid)
            parent_assembly.assemblies.add(a1)
            parent_assembly.save()
            return redirect('viewAssembly', pk=pid)
            
        else:
            a1 = Assembly(name=name, description=description, parent_vehicle=parent_vehicle, isSubassembly=False)
            a1.save()    
            return redirect('viewVehicle', pk=pk)

    if pid != 0:
        parent_assembly = get_object_or_404(Assembly, id=pid)
    else:
        parent_assembly = None


    context = {'parent_vehicle':parent_vehicle, 'parent_assembly':parent_assembly}
    return render(request, 'vehicle_config/createAssembly.html', context) 



def createVehicle(request): 
    if request.method == 'POST':

        name = request.POST['name']
        description = request.POST['description']
        Vehicle.objects.create(name=name, description=description)
        return redirect('/view')
    
    context = {}
    return render(request, 'vehicle_config/createVehicle.html', context)

def createPart(request, pk):
    parent_assembly = get_object_or_404(Assembly, id=pk)

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        part_number = request.POST['part_number']
        Part.objects.create(name=name, description=description, parent_assembly=parent_assembly, part_number=part_number)
        return redirect('viewAssembly', pk=pk)

    context = {'parent_assembly':parent_assembly}
    return render(request, 'vehicle_config/createPart.html', context)



def createSetupParam(request, pk):
    parent_setup = get_object_or_404(Setup, id=pk)

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        value = request.POST['value']
        units = request.POST['units']
        SetupParam.objects.create(name=name, description=description, parent_setup=parent_setup, value=value, units=units)
        return redirect('viewSetup', pk=pk)

    context = {'parent_setup':parent_setup}
    return render(request, 'vehicle_config/createSetupParam.html', context)







# def createVehicle(request): 
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST['description']
#         assemblies = request.POST['assemblies']
#         setups = request.POST['setups']

#         if assemblies == "" and setups == "":
#             v1 = Vehicle(name=name, description=description)
#             v1.save()
#             msg = "Successfully Created Vehicle"
#         else:
#             if assemblies == "":
#                 setups = setups.split(", ")
#                 for s in setups:
#                     if Setup.objects.filter(name=s).exists() == False:
#                         msg = "The following setup does not exist, please retry: " + "'" + s + "'"
#                         return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
#                 v1 = Vehicle(name=name, description=description)
#                 v1.save()

#                 for s in setups:
#                     s1 = Setup.objects.filter(name=s).get()
#                     v1.setups.add(s1)
#                     v1.save()
#                 msg = "Successfully Created Vehicle"
#             elif setups == "":
#                 assemblies = assemblies.split(", ")
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
#                 v1 = Vehicle(name=name, description=description)
#                 v1.save()
#                 for a in assemblies:
#                     a1 = Assembly.objects.filter(name=a).get()
#                     v1.assemblies.add(a1)
#                     v1.save()
#                 msg = "Successfully Created Vehicle"

#             else:
#                 assemblies = assemblies.split(", ")
#                 setups = setups.split(", ")
                
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
#                 for s in setups:
#                     if Setup.objects.filter(name=s).exists() == False:
#                         msg = "The following setup does not exist, please retry: " + "'" + s + "'"
#                         return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})
                
#                 v1 = Vehicle(name=name, description=description)
#                 v1.save()

#                 for s in setups:
#                     s1 = Setup.objects.filter(name=s).get()
#                     v1.setups.add(s1)
#                     v1.save()
                    
#                 for a in assemblies:
#                     a1 = Assembly.objects.filter(name=a).get()
#                     v1.assemblies.add(a1)
#                     v1.save()

#                 msg = "Successfully Created Vehicle"
#         return render(request, 'vehicle_config/createVehicle.html', {'msg':msg})

#     context = {}
#     return render(request, 'vehicle_config/createVehicle.html', context)


# def createSetupParam(request): 
#     if request.method == 'POST':

#         name = request.POST['name']
#         description = request.POST['description']
#         value = request.POST['value']
#         assemblies = request.POST['assemblies']
#         parts = request.POST['parts']
        

#         if assemblies == "" and parts == "":
#             sp1 = SetupParam(name=name, description=description, value=value)
#             sp1.save()
#             msg = "Successfully Created Setup Parameter"
#         else:
#             if assemblies == "":
#                 parts = parts.split(", ")
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
#                 sp1 = SetupParam(name=name, description=description, value=value)
#                 sp1.save()

#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     sp1.setups.add(p1)
#                     sp1.save()
#                 msg = "Successfully Created Setup Parameter"
#             elif parts == "":
#                 assemblies = assemblies.split(", ")
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
#                 sp1 = SetupParam(name=name, description=description, value=value)
#                 sp1.save()
#                 for a in assemblies:
#                     a1 = Assembly.objects.filter(name=a).get()
#                     sp1.assemblies.add(a1)
#                     sp1.save()
#                 msg = "Successfully Created Setup Parameter"

#             else:
#                 assemblies = assemblies.split(", ")
#                 parts = parts.split(", ")
                
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
                
#                 sp1 = SetupParam(name=name, description=description, value=value)
#                 sp1.save()

#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     sp1.setups.add(p1)
#                     sp1.save()
                    
#                 for a in assemblies:
#                     a1 = Assembly.objects.filter(name=a).get()
#                     sp1.assemblies.add(a1)
#                     sp1.save()

#                 msg = "Successfully Created Setup Parameter"
        
#         return render(request, 'vehicle_config/createSetupParam.html', {'msg':msg})
#     context = {}
#     return render(request, 'vehicle_config/createSetupParam.html', context)
    



# def createAssembly(request): 
#     if request.method == 'POST':

#         name = request.POST['name']
#         description = request.POST['description']
#         parts = request.POST['parts']
#         assemblies = request.POST['assemblies']

#         if assemblies == "" and parts == "":
#             a1 = Assembly(name=name, description=description)
#             a1.save()
#             msg = "Successfully Created Assembly"
#         else:
#             if assemblies == "":
#                 parts = parts.split(", ")
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()

#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     a1.setups.add(p1)
#                     a1.save()
#                 msg = "Successfully Created Assembly"
#             elif parts == "":
#                 assemblies = assemblies.split(", ")
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()
#                 for a in assemblies:
#                     subAssembly = Assembly.objects.filter(name=a).get()
#                     a1.assemblies.add(subAssembly)
#                     a1.save()
#                 msg = "Successfully Created Assembly"

#             else:
#                 assemblies = assemblies.split(", ")
#                 parts = parts.split(", ")
                
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()
#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     a1.setups.add(p1)
#                     a1.save()
#                 for a in assemblies:
#                     subAssembly = Assembly.objects.filter(name=a).get()
#                     a1.assemblies.add(subAssembly)
#                     a1.save()
#                 msg = "Successfully Created Assembly"

#         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})

#     context = {}
#     return render(request, 'vehicle_config/createAssembly.html', context)
    
# def editAssembly(request, pk): 
#     assembly = get_object_or_404(Part, id=pk)
#     if request.method == 'POST':

#         name = request.POST['name']
#         description = request.POST['description']
#         parts = request.POST['parts']
#         assemblies = request.POST['assemblies']

#         if assemblies == "" and parts == "":
#             Assembly.objects.filter(pk=assembly.id).update(name=name, description=description, assemblies=assemblies, parts=parts)
            
#             objType = "Assembly"
#             msg =  "ID: " + str(assembly.id) + ", Name: " + str(name) 
#             context = {
#                 'objType': objType,
#                 'msg' : msg
#                 }
#             return render(request, 'vehicle_config/success.html', context)
#         else:
#             if assemblies == "":
#                 parts = parts.split(", ")
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()

#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     a1.setups.add(p1)
#                     a1.save()
#                 msg = "Successfully Created Assembly"
#             elif parts == "":
#                 assemblies = assemblies.split(", ")
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()
#                 for a in assemblies:
#                     subAssembly = Assembly.objects.filter(name=a).get()
#                     a1.assemblies.add(subAssembly)
#                     a1.save()
#                 msg = "Successfully Created Assembly"

#             else:
#                 assemblies = assemblies.split(", ")
#                 parts = parts.split(", ")
                
#                 for a in assemblies:
#                     if Assembly.objects.filter(name=a).exists() == False:
#                         msg = "The following assembly does not exist, please retry: " + "'" + a + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
#                 for p in parts:
#                     if Part.objects.filter(name=p).exists() == False:
#                         msg = "The following part does not exist, please retry: " + "'" + p + "'"
#                         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})
                
#                 a1 = Assembly(name=name, description=description)
#                 a1.save()
#                 for p in parts:
#                     p1 = Part.objects.filter(name=p).get()
#                     a1.setups.add(p1)
#                     a1.save()
#                 for a in assemblies:
#                     subAssembly = Assembly.objects.filter(name=a).get()
#                     a1.assemblies.add(subAssembly)
#                     a1.save()
#                 msg = "Successfully Created Assembly"

#         return render(request, 'vehicle_config/createAssembly.html', {'msg':msg})

#     context = {}
#     return render(request, 'vehicle_config/createAssembly.html', context)





