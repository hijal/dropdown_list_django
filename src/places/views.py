from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Location, City, Place
from .forms import PersonForm

def check(request):
    list_places = Location.objects.all()
    form = PersonForm()
    c = {
        'list_places' : list_places,
        'form' : form
    }
    return render(request, 'places/location.html', c)

def load_cities(request):
    city_id = request.GET.get('city')
    places = Place.objects.filter(city_id=city_id)
    return render(request, 'places/dropdown.html', {'places': places})