from rest_framework import serializers
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
    class Meta:
        model = CollectorProfile
        fields = ('collector_id', 'vehicle', 'work_area', 'timestamp', 'auth')


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
