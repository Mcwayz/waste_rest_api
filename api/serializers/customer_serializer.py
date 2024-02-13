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
