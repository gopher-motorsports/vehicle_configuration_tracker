from django.urls import path, include
# from .views import PartListView, PartDetailView, PartCreateView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view, name='view'),
    
    path('edit/<str:obj>/<int:pk>/success/', views.success, name='success'),

    path('view/Vehicle/<int:pk>/', views.viewVehicle, name='viewVehicle'),
    path('view/Setup/<int:pk>/', views.viewSetup, name='viewSetup'),
    path('view/Setup2/<int:pk>/', views.viewSetup2, name='viewSetup2'),
    path('view/Assembly/<int:pk>/', views.viewAssembly, name='viewAssembly'),
    path('view/Part/<int:pk>/', views.viewPart, name='viewPart'),
    path('view/SetupParam/<int:pk>/', views.viewSetupParam, name='viewSetupParam'),
    path('view/spPart/<int:spPk>/<int:pk>/<str:act>/', views.spPart, name='spPart'),
    path('view/spAssembly/<int:spPk>/<int:pk>/<str:act>/', views.spAssembly, name='spAssembly'),


    path('edit/<str:obj>/<int:pk>/', views.edit, name='edit'),
    path('delete/<str:obj>/<int:pk>/', views.delete, name='delete'),

    path('createVehicle/', views.createVehicle, name='createVehicle'),
    path('createSetup/<int:pk>/', views.createSetup, name='createSetup'),
    path('createAssembly/<int:pk>/<int:pid>/', views.createAssembly, name='createAssembly'),
    path('createPart/<int:pk>/', views.createPart, name='createPart'),

    path('createSetupParam/<int:pk>/', views.createSetupParam, name='createSetupParam'),
    
    
    

]