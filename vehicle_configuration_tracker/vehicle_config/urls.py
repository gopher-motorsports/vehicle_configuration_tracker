from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view, name='view'),
    path('createVehicle/', views.createVehicle, name='createVehicle'),
    path('createSetup/', views.createSetup, name='createSetup'),
    path('createSetupParam/', views.createSetupParam, name='createSetupParam'),
    path('createPart/', views.createPart, name='createPart'),
    path('createAssembly/', views.createAssembly, name='createAssembly'),
]