from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=120)


class Car(models.Model):
    name = models.CharField(max_length=120)
    doors = models.PositiveIntegerField(default=2)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
