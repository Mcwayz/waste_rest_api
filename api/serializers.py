from rest_framework import serializers
from django.contrib.auth import get_user_model
from base.models import Subscription, UserProfile, Waste, Collection, Collectors, TaskAssignment


# Subscription Serializer

class SubSerializer(serializers.ModelSerializer):
    lastname = serializers.SerializerMethodField()
    firstname = serializers.SerializerMethodField()
    address = serializers.CharField(source='user.address')
    auth_id = serializers.IntegerField(source='user.auth_id')
    waste_type = serializers.CharField(source='waste.waste_type')
    monthly_price = serializers.DecimalField(source='waste.monthly_price', max_digits=10, decimal_places=2)

    class Meta:
        model = Subscription
        fields = ('sub_id', 'firstname', 'lastname', 'address', 'waste_type', 'monthly_price', 'sub_date', 'auth_id')

    def get_firstname(self, obj):
        return obj.user.auth.first_name

    def get_lastname(self, obj):
        return obj.user.auth.last_name
    
# Waste Serializer
    
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id','waste_type', 'monthly_price', 'waste_desc')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    class Meta:
        model = UserProfile
        fields = ('user_id', 'address', 'longitude', 'latitude', 'auth_id', 'firstname', 'lastname', 'email')
        
    
# Collection Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('auth', 'address', 'longitude', 'latitude')

class CollectionSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()  # Use the nested serializer for UserProfile
    firstname = serializers.SerializerMethodField()  # Add this line

    class Meta:
        model = Collection
        fields = ('collection_id', 'user', 'firstname', 'lastname', 'is_collected', 'collection_date', 'user_collect_date', 'request_date', 'address', 'longitude', 'latitude')

    def get_firstname(self, obj):
        return obj.user.auth.first_name  # Access the first_name field through the UserProfile relationshipclass UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('auth', 'address', 'longitude', 'latitude')

class CollectionSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    firstname = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ('collection_id', 'user', 'firstname', 'is_collected', 'collection_date', 'user_collect_date', 'request_date')

    def get_firstname(self, obj):
        return obj.user.auth.first_name
        
        
# Profile Serializer

class ProfileSerializer(serializers.ModelSerializer):
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname','address', 'longitude', 'latitude', 'auth_id')
        
# Subscription Serializer
        
class SubscriptionSerializer(serializers.ModelSerializer):
    waste = serializers.PrimaryKeyRelatedField(queryset=Waste.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    class Meta:
        model = Subscription
        fields = ('sub_id', 'waste', 'sub_date', 'user')

# Collection Serializer

class CollectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Collection
        fields = ('collection_id', 'user', 'is_collected', 'request_date', 'user_collect_date', 'collection_date')
        
        
# Details Serializer

class DetailsSerializer(serializers.ModelSerializer):
    auth_id = serializers.SerializerMethodField()
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')

    def get_auth_id(self, obj):
        return obj.auth_id if obj.auth else None

    class Meta:
        model = UserProfile
        fields = ('user_id', 'address', 'longitude', 'latitude', 'auth_id', 'firstname', 'lastname', 'email')
        
        
# Collection Serializer

class CollectorDetailsSerializer(serializers.ModelSerializer):
    auth_id = serializers.SerializerMethodField()
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')

    def get_auth_id(self, obj):
        return obj.auth_id if obj.auth else None

    class Meta:
        model = Collectors
        fields = ('collector_id', 'vehicle', 'work_area', 'firstname', 'lastname', 'email', 'auth_id')
        
        
# Collection Serializer
        
class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectors
        fields = ('collector_id', 'vehicle', 'work_area', 'auth')


# Tasks Serializer
        
class TasksSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.address')
    latitude = serializers.CharField(source='user.latitude')
    longitude = serializers.CharField(source='user.longitude')
    request_date = serializers.CharField(source='collection.request_date')
    is_collected = serializers.CharField(source='collection.is_collected')
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    user_collect_date = serializers.CharField(source='collection.user_collect_date')
    collection_id = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    class Meta:
        model = TaskAssignment
        fields = ('task_id', 'collection_id', 'collector_id','user', 'address', 'longitude', 'latitude', 'is_collected','request_date', 'assigned_date', 'user_collect_date', 'date_closed')
        
        
 # Collection Serializer
        
class CollectorsSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='auth.email')
    lastname = serializers.CharField(source='auth.last_name')
    firstname = serializers.CharField(source='auth.first_name')
    class Meta:
        model = Collectors
        flelds = ('collector_id', 'firstname', 'lastname', 'email', 'vehicle', 'work_area')
        
  # Task Assignment Serializer
        
class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = ('task_id', 'collector', 'collection', 'user', 'assigned_date', 'date_closed')