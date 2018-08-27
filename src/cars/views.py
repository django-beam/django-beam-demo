import beam

from .models import Car, Brand, Passenger


class PassengerInline(beam.RelatedInline):
    title = 'Passengers'
    foreign_key_field = 'car'
    model = Passenger
    fields = ['name', 'origin', 'destination']


class DetailPassengerInline(PassengerInline):
    fields = ['origin', 'destination']


class CarViewSet(beam.ViewSet):
    model = Car
    fields = ["name", "brand", ]
    detail_fields = ["name", "brand", "wheels", "fuel"]

    inline_classes = [PassengerInline]
    detail_inline_classes = [DetailPassengerInline]


class BrandViewSet(beam.ViewSet):
    model = Brand
    fields = ["name", "logo"]
