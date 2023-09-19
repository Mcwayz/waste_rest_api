import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from base.models import CustomerProfile, Collection, Waste, CollectorProfile, Requests, Ratings
from ..serializers.collector_serializer import WasteSerializer, CollectorWasteSerializer, CustomerSerializer, CollectorDetailsSerializer, RequestSerializer, CollectionSerializer, CollectorLocationUpdateSerializer


#                            #
#                            #
#                            #
#    GET Request Methods     #
#                            #
#                            #
#                            #


# Get Customer Requests
@api_view(['GET'])
def getRequests(request):
    status = request.data.get('request_status')
    requests = Requests.objects.filter(request_status=status)
    serializer = WasteSerializer(requests, many=True)
    return Response(serializer.data) 


# Get Collector Profile
@api_view(['GET'])
def getCollectorProfile(request, pk):
    profile = get_object_or_404(CollectorProfile, pk=pk)
    serializer = CollectorDetailsSerializer(profile, many=True)
    return Response(serializer.data)


# Get Completed Collections 
@api_view(['GET'])
def getCompletedCollections(request, pk):
    collections = Requests.objects.filter(collector=pk)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


# Get Collector Ratings
@api_view(['GET'])
def getCollectorRatings(request, pk):
    ratings = Ratings.objects.filter(collector=pk)
    serializer = CollectionSerializer(ratings, many=True)
    return Response(serializer.data)


#                            #
#                            #
#                            #
# End Of GET Request Methods #
#                            #
#                            #
#                            # 


# Approve Collection Request
@api_view(['PUT'])
def claimRequest(request):
    request_id = request.data.get('request_id')
    new_status = 'Claimed'
    
    try:
        # Get the request object to update
        request_to_update = Requests.objects.get(pk=request_id)
        request_to_update.request_status = new_status
        request_to_update.save()
        
        return Response({"Message": "Collection Request Updated And Status Claimed."}, status=status.HTTP_200_OK)
    
    except Requests.DoesNotExist:
        return Response({"Message": "Collection Request Not Found."}, status=status.HTTP_404_NOT_FOUND)
    
    
# Update Collector Location
@api_view(['PUT'])
def updateCollectorLocation(request, collector_id):
    try:
        collector_profile = CollectorProfile.objects.get(pk=collector_id)
    except CollectorProfile.DoesNotExist:
        return Response({"Message": "Collector Profile Not Found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CollectorLocationUpdateSerializer(collector_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Collector Location Updated Successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Add Collection
@api_view(['POST'])
def addCollection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Add Collector Profile
@api_view(['POST'])
def addCollectorProfile(request):
    serializer = CollectorDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    