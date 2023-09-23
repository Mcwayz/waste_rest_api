from django.db.models import F
from django.db.models import FloatField
from base.models import CollectorProfile
from django.db.models.functions import Cos, Radians, Sin


def get_collectors_within_radius(customer_latitude, customer_longitude, radius_km=10):
    # Convert latitude and longitude to radians
    customer_latitude = Radians(F(customer_latitude, output_field=FloatField()))
    customer_longitude = Radians(F(customer_longitude, output_field=FloatField()))

    # Calculate the distance formula
    collectors = CollectorProfile.objects.annotate(
        distance=6371 * Cos(
            Cos(customer_latitude) * Cos(Radians(F('latitude', output_field=FloatField()))) *
            Cos(customer_longitude - Radians(F('longitude', output_field=FloatField()))) +
            Sin(customer_latitude) * Sin(Radians(F('latitude', output_field=FloatField())))
        )
    ).filter(distance__lte=radius_km).order_by('distance')

    return collectors