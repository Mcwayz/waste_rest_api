import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import CustomerProfile, CollectorProfile, Requests, Ratings, Collection
from ..serializers.collector_serializer import CollectorSerializer, RequestSerializer, CollectionSerializer, UserSerializer, CollectorsSerializer



# GET Request Methods



# Get Customer Requests


@api_view(['GET'])
def getRequests(request):
    status = request.query_params.get('request_status')
    requests = Requests.objects.filter(request_status=status)
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data) 



# Get Collector Profile


@api_view(['GET'])
def getCollectorProfile(request, pk):
    profile = get_object_or_404(CollectorProfile, pk=pk)
    serializer = CollectorSerializer(profile)
    return Response(serializer.data)



# Get Collector Profiles


@api_view(['GET'])
def getCollectorProfiles(request):
    profiles = CollectorProfile.objects.all()
    serializer = CollectorsSerializer(profiles, many=True)
    return Response(serializer.data)


# Get Completed Collections 


@api_view(['GET'])
def getCompletedCollections(request, pk):
    collections = Collection.objects.filter(collector=pk)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


# Get Collector Ratings


@api_view(['GET'])
def getCollectorRatings(request, pk):
    ratings = Ratings.objects.filter(collector=pk)
    serializer = CollectionSerializer(ratings, many=True)
    return Response(serializer.data)


# End Of GET Request Methods


# POST Request Methods


# Add Collection

@api_view(['POST'])
def addCollection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Cancelling a Collection Request


@api_view(['POST']) 
def cancel_request(request, request_id):
    request_obj = get_object_or_404(Requests, pk=request_id)
    if request.user != request_obj.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
    request_obj.request_status = 'Cancelled'
    request_obj.save()
    return Response({'Message': 'Request Cancelled Successfully'}, status=status.HTTP_200_OK)



# Add Collector Profile


@api_view(['POST'])
def create_user_and_profile(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            vehicle = request.data.get('vehicle')
            work_area = request.data.get('work_area')
            profile_data = {'vehicle': vehicle, 'work_area': work_area,'auth': user_instance}
            profile_serializer = CollectorSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({'Message': 'User and Profile Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                user_instance.delete()
                return Response({'Error': 'Profile Creation Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# End Of POST Methods



# PUT Request Methods



# Update Customer Request Location


@api_view(['PUT'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(user_id=pk)
    serializer = CollectorSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Complete Collection


@api_view(['PUT'])
def completeCollection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collection.complete = True
    collection.save()
    return Response({'Message': 'Collection Marked as Complete'}, status=status.HTTP_200_OK)


# Approve Collection Request


@api_view(['PUT'])
def claimRequest(request):
    request_id = request.data.get('request_id')
    new_status = 'Claimed'
    
    try:
        request_to_update = Requests.objects.get(pk=request_id)
        request_to_update.request_status = new_status
        request_to_update.save()
        return Response({"Message": "Collection Request Updated And Status Claimed."}, status=status.HTTP_200_OK)

    except Requests.DoesNotExist:
        return Response({"Message": "Collection Request Not Found."}, status=status.HTTP_404_NOT_FOUND)


# End Of PUT Request Methods
