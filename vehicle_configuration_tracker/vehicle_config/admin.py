from django.contrib import admin
from .models import Setup, Vehicle, Part, Assembly, SetupParam




admin.site.register(Part)
admin.site.register(Assembly)
admin.site.register(SetupParam)
admin.site.register(Vehicle)
admin.site.register(Setup)



