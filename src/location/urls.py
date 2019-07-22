from django.contrib import admin
from django.urls import path

from places.views import  load_cities, check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', check),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]
