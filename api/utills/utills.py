from django.db.models import F, Func, FloatField
from base.models import CollectorProfile
from django.db.models.functions import Radians, Sin, Cos, ACos

EARTH_RADIUS_KM = 6371  # Earth radius in kilometers

def get_collectors_within_radius(customer_latitude, customer_longitude, radius_km=10):
    # Convert latitude and longitude to radians
    customer_latitude_rad = Radians(Func(F(customer_latitude)))
    customer_longitude_rad = Radians(Func(F(customer_longitude)))

    # Calculate the distance formula using Haversine formula
    collectors = CollectorProfile.objects.annotate(
        dlat=Radians(F('latitude')) - customer_latitude_rad,
        dlon=Radians(F('longitude')) - customer_longitude_rad,
        a=Sin(Func(F('dlat') / 2)) ** 2 +
          Cos(customer_latitude_rad) * Cos(Radians(F('latitude'))) *
          Sin(Func(F('dlon') / 2)) ** 2,
        c=2 * ACos(Sin(Func(F('a') ** 0.5 / 2)))
    ).annotate(
        distance=EARTH_RADIUS_KM * F('c')
    ).filter(distance__lte=radius_km).order_by('distance')

    return collectors