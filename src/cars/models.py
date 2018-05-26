from django.db import models
from django.utils.translation import ugettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(null=True, blank=True, upload_to="brands/")

    def __str__(self):
        return self.name


class Car(models.Model):
    FUEL_ELECTRIC = "electric"
    FUEL_GASOLINE = "diesel"
    FUEL_CHOICES = [(FUEL_ELECTRIC, _("Electric")), (FUEL_GASOLINE, _("Diesel"))]

    name = models.CharField(max_length=120)
    doors = models.PositiveIntegerField(default=2, blank=True)
    fuel = models.CharField(max_length=120, choices=FUEL_CHOICES, default=FUEL_ELECTRIC)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return "{brand} - {name}".format(name=self.name, brand=self.brand.name)
