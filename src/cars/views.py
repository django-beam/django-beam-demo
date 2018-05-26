import beam

from .models import Car, Brand


class CarViewSet(beam.ViewSet):
    model = Car
    fields = ["name", "wheels"]


class BrandViewSet(beam.ViewSet):
    model = Brand
    fields = ["name"]
