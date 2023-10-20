from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Ratings, CustomerProfile, Waste, Collection, CollectorProfile, Requests

# Waste Serializer
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id', 'waste_type', 'collection_price', 'waste_desc')

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    # Include user-related fields directly or reference them using UserSerializer
    class Meta:
        model = CustomerProfile
        fields = ('customer_id', 'latitude', 'longitude', 'address')

# Collector Serializer
class CollectorSerializer(serializers.ModelSerializer):
    # Include user-related fields directly or reference them using UserSerializer
    class Meta:
        model = CollectorProfile
        fields = ('collector_id', 'vehicle', 'work_area', 'latitude', 'longitude', 'timestamp')

# User Serializer (for referencing user-related fields)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name')

# Request Serializer
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('customer', 'waste', 'number_of_bags', 'request_status', 'collection_price')

# Rating Serializer
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('rating_score', 'collection')
        depth = 1  # Include details of the related collection

# Collection Serializer
class CollectionSerializer(serializers.ModelSerializer):
    # Include collector details using CollectorSerializer or just reference collector_id
    collector = CollectorSerializer()

    class Meta:
        model = Collection
        fields = ('collection_id', 'request', 'collector', 'request_date', 'collection_date', 'collection_price')
        
# Collector Location Serializer
        
class CustomerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('latitude', 'longitude')
