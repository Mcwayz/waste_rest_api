from django.db.models import F, Func, FloatField
from base.models import CollectorProfile
from django.db.models.functions import Radians, Sin, Cos, ACos

EARTH_RADIUS_KM = 6371  # Earth radius in kilometers

def get_collectors_within_radius(customer_latitude, customer_longitude, radius_km=10):
    # Convert latitude and longitude to radians
    customer_latitude_rad = Radians(Func(F(customer_latitude, output_field=FloatField())))
    customer_longitude_rad = Radians(Func(F(customer_longitude, output_field=FloatField())))

    # Calculate the distance formula using Haversine formula
    collectors = CollectorProfile.objects.annotate(
        dlat=Radians(F('latitude', output_field=FloatField())) - customer_latitude_rad,
        dlon=Radians(F('longitude', output_field=FloatField())) - customer_longitude_rad,
        a=Sin(Func(F('dlat', output_field=FloatField()) / 2)) ** 2 +
          Cos(customer_latitude_rad) * Cos(Radians(F('latitude', output_field=FloatField()))) *
          Sin(Func(F('dlon', output_field=FloatField()) / 2)) ** 2,
        c=2 * ACos(Func(Sin(Func(F('a', output_field=FloatField()) ** 0.5 / 2))),
                   output_field=FloatField())
    ).annotate(
        distance=EARTH_RADIUS_KM * F('c', output_field=FloatField())
    ).filter(distance__lte=radius_km).order_by('distance')

    return collectors
