from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view, name='view'),
    path('createVehicle/', views.createVehicle, name='createVehicle'),
    path('createSetup/', views.createSetup, name='createSetup'),
]