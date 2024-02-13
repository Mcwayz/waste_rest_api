from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Ratings, CustomerProfile, Waste, Collection, CollectorProfile, Requests


# Waste Serializer
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = '__all__'
        

# Customer Serializer

class CustomerProfileSerializer(serializers.ModelSerializer):
    auth = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = CustomerProfile
        fields = ['customer_id', 'address', 'auth']



# Customer Serializer

class CustomerProfilesSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='auth.username')
    email = serializers.EmailField(source='auth.email')
    first_name = serializers.CharField(source='auth.first_name')
    last_name = serializers.CharField(source='auth.last_name')
    address = serializers.CharField()

    class Meta:
        model = CustomerProfile
        fields = ['customer_id', 'username', 'email', 'first_name', 'last_name', 'address']


# User Serializer (for referencing user-related fields)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user.id  # Return just the user ID
    

# Request Serializer

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'


# Rating Serializer

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

# Collection Serializer

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

# Collector Profile Serializer
class CollectorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorProfile
        fields = '__all__'


# Completed Task Serialiser
    
class CompletedCollectionSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    request_status = serializers.CharField(source='request.request_status')
    request_date = serializers.DateTimeField(source='request.request_date')
    collection_date = serializers.DateTimeField()
    collection_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='request.collection_price')
    waste = serializers.CharField(source='request.waste.waste_type')
    customer_name = serializers.SerializerMethodField()
    collector_name = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ('request_id', 'location', 'request_status', 'request_date', 'collection_date', 'collection_price', 'waste', 'customer_name', 'collector_name')

    def get_location(self, obj):
        return obj.request.customer.address

    def get_customer_name(self, obj):
        return f"{obj.request.customer.auth.first_name} {obj.request.customer.auth.last_name}"

    def get_collector_name(self, obj):
        return f"{obj.collector.auth.first_name} {obj.collector.auth.last_name}"