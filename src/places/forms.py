from django import forms
from .models import Location, City, Place

class PersonForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'place')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].queryset = Place.objects.none()

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['place'].queryset = Place.objects.filter(city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['place'].queryset = self.instance.city.place_set.order_by('name')
