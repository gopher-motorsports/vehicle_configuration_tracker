import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

class VehicleFilter(django_filters.FilterSet):
    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    
    name = CharFilter(field_name="name", lookup_expr="icontains", label="Vehicle ")
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ['deleted', 'date_modifed', 'description', 'date_created']