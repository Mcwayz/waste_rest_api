from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Waste, CollectorProfile, CollectorWaste, Requests, Collection

# Waste Type Serializer

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id', 'waste_type', 'waste_desc', 'collection_price')



# Collector Categories Serializer

class CollectorWasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorWaste
        fields = ('collector', 'waste')


# Collector Serializer

class CollectorSerializer(serializers.ModelSerializer):
    auth = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = CollectorProfile
        fields = ('collector_id', 'vehicle', 'work_area', 'timestamp', 'auth')
        
        
        
# Collector Serializer

class CollectorsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='auth.username')
    email = serializers.EmailField(source='auth.email')
    first_name = serializers.CharField(source='auth.first_name')
    last_name = serializers.CharField(source='auth.last_name')
    class Meta:
        model = CollectorProfile
        fields = ('collector_id',  'username', 'email', 'first_name', 'last_name','vehicle', 'work_area', 'timestamp')



# Request Serializer

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('request_id', 'location', 'number_of_bags', 'request_status', 'request_date', 'waste', 'collection_price', 'customer')


# Collection Serializer

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('collection_id', 'collection_date', 'request', 'collector')


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