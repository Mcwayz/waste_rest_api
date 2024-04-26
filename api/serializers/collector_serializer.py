
from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Waste, CollectorProfile, Requests, Collection, Wallet


# Waste Type Serializer


class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_id', 'waste_type', 'waste_desc', 'collection_price')


# Collector Serializer


class CollectorSerializer(serializers.ModelSerializer):
    auth = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    waste = serializers.PrimaryKeyRelatedField(queryset=Waste.objects.all())
    class Meta:
        model = CollectorProfile
        fields = ('collector_id', 'vehicle', 'work_area', 'timestamp', 'auth', 'waste')


# Collector Serializer


class CollectorsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='auth.username')
    email = serializers.EmailField(source='auth.email')
    first_name = serializers.CharField(source='auth.first_name')
    last_name = serializers.CharField(source='auth.last_name')
    waste = serializers.CharField(source='waste.waste_type')
    class Meta:
        model = CollectorProfile
        fields = ('collector_id',  'username', 'email', 'first_name', 'last_name','vehicle', 'work_area', 'waste', 'timestamp')


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
        return user.id 


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


# Wallet Serializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


# Collector Data Serializer


class CollectorDataSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='auth.first_name') 
    last_name = serializers.CharField(source='auth.last_name')  
    vehicle = serializers.CharField()                             
    work_area = serializers.CharField()                           
    waste = serializers.CharField(source='waste.waste_type')      
    wallet_balance = serializers.DecimalField(max_digits=10, decimal_places=2, source='wallet.balance') 
    wallet_id = serializers.IntegerField(source='wallet.wallet_id')

    class Meta:
        model = CollectorProfile 
        fields = ('wallet_id','first_name', 'last_name', 'vehicle', 'work_area', 'waste', 'wallet_balance') 

