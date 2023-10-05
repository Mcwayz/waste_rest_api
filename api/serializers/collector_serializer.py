from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from base.models import Ratings, CustomerProfile, Waste, CollectorProfile, CollectorWaste, Requests, Collection

    
# Waste Type Serializer
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id','waste_type', 'collection_price', 'waste_desc')
        
        
# Collector Categories Serializer
class CollectorWasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorWaste
        fields = ('collector', 'waste')
        
# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    class Meta:
        model = CustomerProfile
        fields = ('customer','firstname', 'lastname', 'email', 'latitude', 'longitude', 'address')


# Collector Serializer
class CollectorDetailsSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='auth.email')
    auth_id = serializers.IntegerField(source='auth.id')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    
    class Meta:
        model = CollectorProfile
        fields = ('collector_id', 'auth_id', 'vehicle', 'work_area', 'firstname', 'lastname', 'email', 'longitude', 'latitude')




        
        
# Request Serializer
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('customer', 'waste', 'number_of_bags', 'request_status', 'collection_price')
        
# Collection Serializer
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('collection_id', 'collection_date', 'collection_price', 'request', 'collector')
        
        
# Collector Location Serializer
        
class CollectorLocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorProfile
        fields = ('latitude', 'longitude')