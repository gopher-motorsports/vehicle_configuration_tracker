from django.shortcuts import render, redirect
from datetime import datetime
from .models import Vehicle, Setup, Part, Assembly, SetupParam
import json
from django.core import serializers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.http import HttpResponseRedirect
from .filters import VehicleFilter
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
    vehicles = Vehicle.objects.all()
    myFilter = VehicleFilter(request.GET, queryset=vehicles)
    vehicles = myFilter.qs
    
    # vehicles = Vehicle.objects.all()
    # vehicles = serializers.serialize("json",vehicles)
    # setups = Setup.objects.all()
    # setups = serializers.serialize("json",setups)
    # context = {
    #     'vehicles' : json.dumps(vehicles),
    #     'setups' : json.dumps(setups)
    # }
    context = {
    'myFilter': myFilter,
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
        'assemblies': vehicle.assembly_set.all().filter(isSubassembly=False),
        'setups': vehicle.setup_set.all()
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
        'assemblies': vehicle.assembly_set.all().filter(isSubassembly=False),
        'setups': vehicle.setup_set.all()
    }
    return render(request, 'vehicle_config/viewVehicle.html', context)

def viewSetup(request, pk):
    setup = get_object_or_404(Setup, id=pk)
    obj = "Setup"
    setup_params = setup.setupparam_set.all()
    if request.method == 'POST':
        context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
        return render(request, 'vehicle_config/viewSetup.html', context)
    
    
    context = {'id': setup.id, 'setup':setup, 'obj':obj, 'setup_params':setup_params}
    return render(request, 'vehicle_config/viewSetup.html', context)

def viewAssembly(request, pk):
    assembly = get_object_or_404(Assembly, id=pk)
    sub_assemblies = assembly.assemblies.all()
    obj = "Assembly"
    
    #parent_vehicle_id = assembly.parent_vehicle
    parts = assembly.part_set.all()
    if request.method == 'POST':
        context = {'id': assembly.id, 'assembly':assembly, 'obj':obj, 'parts':parts, 'sub_assemblies':sub_assemblies}
        return render(request, 'vehicle_config/viewAssembly.html', context)
    
    
    context = {'id': assembly.id, 'assembly':assembly, 'obj':obj, 'parts':parts, 'sub_assemblies':sub_assemblies}
    return render(request, 'vehicle_config/viewAssembly.html', context)


def viewPart(request, pk):
    part = get_object_or_404(Part, id=pk)
    obj = "Part"
    parent_assembly = part.parent_assembly.name
    #parent_vehicle_id = assembly.parent_ve
    if request.method == 'POST':
        context = {'id': part.id, 'name':part.name, 'obj':obj, 'part':part, 'parent_assembly':parent_assembly}
        return render(request, 'vehicle_config/viewPart.html', context)
    
    
    context = {'id': part.id, 'name':part.name, 'obj':obj, 'part':part, 'parent_assembly':parent_assembly}
    return render(request, 'vehicle_config/viewPart.html', context)

def viewSetupParam(request, pk):
    setupParam = get_object_or_404(SetupParam, id=pk)
 
    obj = "SetupParam"
    
    #parent_vehicle_id = assembly.parent_vehicle
    parts = setupParam.parts.all()
    assemblies = setupParam.assemblies.all()
    parent_setup = setupParam.parent_setup.name
    

    if request.method == 'POST':
        context = {'id': setupParam.id, 'setupParam':setupParam, 'obj':obj, 'parts':parts, 'assemblies':assemblies, 'parent_setup':parent_setup}
        return render(request, 'vehicle_config/viewSetupParam.html', context)
    
    
    context = {'id': setupParam.id, 'setupParam':setupParam, 'obj':obj, 'parts':parts, 'assemblies':assemblies, 'parent_setup':parent_setup}
    return render(request, 'vehicle_config/viewSetupParam.html', context)






# def editPart(request, pk): 
#     part = get_object_or_404(Part, id=pk)
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST['description']
#         Part.objects.filter(pk=part.id).update(name=name, description=description)

#         objType = "Part"
#         msg =  "ID: " + str(part.id) + ", Name: " + str(name) 
#         context = {
#             'objType': objType,
#             'msg' : msg
#         }
#         return render(request, 'vehicle_config/success.html', context)
        
        
#     context = {'id': part.id, 'name': part.name, 'description': part.description}
#     return render(request, 'vehicle_config/editPart.html', context)

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
    else:
        return render(request, 'vehicle_config/success.html', context)



def edit(request, obj, pk):
     
    actual_obj = get_object_or_404(eval(obj), id=pk)
    if request.method == 'POST': 
        name = request.POST['name']
        description = request.POST['description']

        eval(obj).objects.filter(pk=actual_obj.id).update(name=name, description=description)

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
        
        
    context = {'id': actual_obj.id, 'obj': obj, 'name': actual_obj.name, 'description': actual_obj.description}
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
            actual_obj.delete()
            return redirect('viewVehicle', pk=parent_vehicle)

    context = {'id': actual_obj.id, 'name': actual_obj.name, 'description': actual_obj.description, 'obj':obj}
    return render(request, 'vehicle_config/delete.html', context)

        


def createSetup(request, pk):
    parent_vehicle = get_object_or_404(Vehicle, id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Setup.objects.create(name=name, description=description, parent_vehicle=parent_vehicle)
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
        Part.objects.create(name=name, description=description, parent_assembly=parent_assembly)
        return redirect('viewAssembly', pk=pk)

    context = {'parent_assembly':parent_assembly}
    return render(request, 'vehicle_config/createPart.html', context)

def createSetupParam(request, pk):
    parent_setup = get_object_or_404(Setup, id=pk)

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        value = request.POST['value']
        SetupParam.objects.create(name=name, description=description, parent_setup=parent_setup, value=value)
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





