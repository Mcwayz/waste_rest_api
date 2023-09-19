from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Ratings, UserProfile, Waste, Collection, Collectors, Requests

    
# Waste Serializer
    
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id','waste_type', 'collection_price', 'waste_desc')


# User Serializer
class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    class Meta:
        model = UserProfile
        fields = ('user_id', 'address', 'longitude', 'latitude', 'auth_id', 'firstname', 'lastname', 'email')