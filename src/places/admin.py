from django.contrib import admin

from .models import Location, City, Place


admin.site.register(Location)
admin.site.register(City)
admin.site.register(Place)