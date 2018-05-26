import beam

from .models import Car, Brand


class CarViewSet(beam.ViewSet):
    model = Car
    fields = ["name", "brand"]
    detail_fields = ["name", "brand", "wheels", "fuel"]


class BrandViewSet(beam.ViewSet):
    model = Brand
    fields = ["name", "logo"]
