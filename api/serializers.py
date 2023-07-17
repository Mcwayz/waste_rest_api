from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from base.models import Subscription, UserProfile, Waste, Collection, Collectors, TaskAssignment


class SubSerializer(serializers.ModelSerializer):
    firstname = serializers.SerializerMethodField()
    lastname = serializers.SerializerMethodField()
    address = serializers.CharField(source='user.address')
    waste_type = serializers.CharField(source='waste.waste_type')
    auth_id = serializers.IntegerField(source='user.auth_id')
    monthly_price = serializers.DecimalField(source='waste.monthly_price', max_digits=10, decimal_places=2)

    class Meta:
        model = Subscription
        fields = ('sub_id', 'firstname', 'lastname', 'address', 'waste_type', 'monthly_price', 'sub_date', 'auth_id')

    def get_firstname(self, obj):
        return obj.user.auth.first_name

    def get_lastname(self, obj):
        return obj.user.auth.last_name
    
    
class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id','waste_type', 'monthly_price', 'waste_desc')


class UserSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='auth.first_name')
    lastname = serializers.CharField(source='auth.last_name')
    email = serializers.CharField(source='auth.email')
    class Meta:
        model = UserProfile
        fields = ('user_id', 'address', 'longitude', 'latitude', 'auth_id', 'firstname', 'lastname', 'email')
    
        
class CollectionSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.address')
    longitude = serializers.CharField(source='user.longitude')
    latitude = serializers.CharField(source='user.latitude')
    class Meta:
        model = Collection
        fields = ('collection_id', 'user_id', 'is_collected', 'collection_date', 'user_collect_date', 'request_date','address', 'longitude', 'latitude')
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('address', 'longitude', 'latitude', 'auth_id')
        
        
class SubscriptionSerializer(serializers.ModelSerializer):
    waste = serializers.PrimaryKeyRelatedField(queryset=Waste.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Subscription
        fields = ('sub_id', 'waste', 'sub_date', 'user')

    
class CollectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = Collection
        fields = ('collection_id', 'user', 'is_collected', 'request_date', 'user_collect_date', 'collection_date')
        
        
class DetailsSerializer(serializers.ModelSerializer):
    auth_id = serializers.SerializerMethodField()
    firstname = serializers.CharField(source='auth.first_name')
    lastname = serializers.CharField(source='auth.last_name')
    email = serializers.CharField(source='auth.email')

    def get_auth_id(self, obj):
        return obj.auth_id if obj.auth else None

    class Meta:
        model = UserProfile
        fields = ('user_id', 'address', 'longitude', 'latitude', 'auth_id', 'firstname', 'lastname', 'email')
        
        
class CollectorDetailsSerializer(serializers.ModelSerializer):
    auth_id = serializers.SerializerMethodField()
    firstname = serializers.CharField(source='auth.first_name')
    lastname = serializers.CharField(source='auth.last_name')
    email = serializers.CharField(source='auth.email')

    def get_auth_id(self, obj):
        return obj.auth_id if obj.auth else None

    class Meta:
        model = Collectors
        fields = ('collector_id', 'vehicle', 'work_area', 'firstname', 'lastname', 'email', 'auth_id')
        
        
class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectors
        fields = ('collector_id', 'vehicle', 'work_area', 'auth')
        
        
class TasksSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())
    address = serializers.CharField(source='user.address')
    longitude = serializers.CharField(source='user.longitude')
    latitude = serializers.CharField(source='user.latitude')
    user_collect_date = serializers.CharField(source='collection.user_collect_date')
    request_date = serializers.CharField(source='collection.request_date')
    is_collected = serializers.CharField(source='collection.is_collected')
    collection_id = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    class Meta:
        model = TaskAssignment
        fields = ('task_id', 'collection_id', 'collector_id','user', 'address', 'longitude', 'latitude', 'is_collected','request_date', 'assigned_date', 'user_collect_date', 'date_closed')
        
        
class CollectorsSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='auth.first_name')
    lastname = serializers.CharField(source='auth.last_name')
    email = serializers.CharField(source='auth.email')
    
    class Meta:
        model = Collectors
        flelds = ('collector_id', 'firstname', 'lastname', 'email', 'vehicle', 'work_area')
        
        
class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = ('task_id', 'collector', 'collection', 'user', 'assigned_date', 'date_closed')