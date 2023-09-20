import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from ..utills.utills import get_collectors_within_radius
from base.models import CustomerProfile, Collection, Waste, CollectorProfile, Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, CustomerSerializer, CollectorSerializer, UserSerializer, RequestSerializer, RatingSerializer, CollectionSerializer, CustomerLocationSerializer


#                            #
#                            #
#                            #
#    GET Request Methods     #
#                            #
#                            #
#                            #


# Get Waste Types

@api_view(['GET'])
def getWaste(request):
    waste = Waste.objects.all()
    serializer = WasteSerializer(waste, many=True)
    return Response(serializer.data) 


# Get Customer Collection

@api_view(['GET'])
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)

# Customer to view available Collectors within the area.

@api_view(['POST'])
def viewAvailableDrivers(request):
    serializer = CustomerLocationSerializer(data=request.data)
    
    if serializer.is_valid():
        latitude = serializer.validated_data['latitude']
        longitude = serializer.validated_data['longitude']
        
        # Query available collectors within a radius (e.g., 10 kilometers)
        collectors = get_collectors_within_radius(latitude, longitude, radius_km=10)
        
        # Serialize the collector profiles
        collector_data = CollectorSerializer(collectors, many=True).data
        
        return Response(collector_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Update Customer Location

@api_view(['PUT'])
def updateCustomerLocation(request, customer_id):
    try:
        customer_profile = RequestSerializer.objects.get(customer_id=customer_id)
        #Check if the customer id exisits in the profile
    except CustomerProfile.DoesNotExist:
        return Response({"Message": "Customer Profile Not Found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomerLocationSerializer(customer_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Customer Request Location Updated Successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



    
