from django.db import models

class City(models.Model):
    name        = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Place(models.Model):
    city        = models.ForeignKey(City, on_delete=models.CASCADE)
    name        = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    city        = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    place        = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)