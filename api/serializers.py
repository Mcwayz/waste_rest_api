from rest_framework import serializers
from base.models import Subscription, User, Waste, Collection

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = ('waste_type', 'monthly_price', 'waste_desc')


class SubSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='user.firstname')
    lastname = serializers.CharField(source='user.lastname')
    address = serializers.CharField(source='user.address')
    waste_type = serializers.CharField(source='waste.waste_type')
    monthly_price = serializers.DecimalField(source='waste.monthly_price', max_digits=10, decimal_places=2)
    class Meta:
        model = Subscription
        fields = ('sub_id', 'firstname', 'lastname', 'address', 'waste_type', 'monthly_price', 'sub_date')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'firstname', 'lastname', 'address', 'longitude', 'latitude')
        

class CollectionSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.address')
    longitude = serializers.CharField(source='user.longitude')
    latitude = serializers.CharField(source='user.latitude')
    class Meta:
        model = Collection
        fields = ('collection_id', 'is_collected', 'request_date','address', 'longitude', 'latitude')