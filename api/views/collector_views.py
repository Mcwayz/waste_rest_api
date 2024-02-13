import json
from rest_framework import status
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import CustomerProfile, CollectorProfile, Requests, Ratings, Collection
from ..serializers.collector_serializer import CollectorSerializer, CompletedCollectionSerializer, CollectionSerializer, UserSerializer, CollectorsSerializer



# GET Request Methods



# Get Customer Requests

@api_view(['GET'])
def get_customer_requests(request): 
    customer_requests = Requests.objects.select_related('customer__auth').all()
    serialized_requests = []
    for request_obj in customer_requests:
        serialized_request = {
            'request_id': request_obj.request_id,
            'location': request_obj.location,
            'number_of_bags': request_obj.number_of_bags,
            'request_status': request_obj.request_status,
            'request_date': request_obj.request_date,
            'collection_price': str(request_obj.collection_price),
            'waste': request_obj.waste_id,
            'first_name': request_obj.customer.auth.first_name,
            'last_name': request_obj.customer.auth.last_name
        }
        serialized_requests.append(serialized_request)
    
    return Response(serialized_requests)



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
def collections_by_collector(request, collector_id):
    try:
        collections = Collection.objects.filter(collector_id=collector_id)
        serializer = CompletedCollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        return Response({"Message": "Collections Not Found For This Collector."}, status=status.HTTP_404_NOT_FOUND)


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
        request_id = request.data.get('request')
        new_status = request.data.get('status')
        success, message = update_request_status(request_id, new_status)
        if success:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": message}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Functional Update Status Function


def update_request_status(request_id, new_status):
    try:
        request_to_update = Requests.objects.get(pk=request_id)
        request_to_update.request_status = new_status
        request_to_update.save()
        return True, "Collection Request Updated And Status Changed."
    except Requests.DoesNotExist:
        return False, "Collection Request Not Found."


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
            waste = request.data.get('waste') 
            profile_data = {'vehicle': vehicle, 'work_area': work_area,'auth': user_instance, 'waste':waste}
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



# Update Collection Request


@api_view(['PUT'])
def updateRequest(request):
    request_id = request.data.get('request_id')
    new_status = request.data.get('status')
    try:
        request_to_update = Requests.objects.get(pk=request_id)
        request_to_update.request_status = new_status
        request_to_update.save()
        return Response({"Message": "Collection Request Updated And Status Changed."}, status=status.HTTP_200_OK)

    except Requests.DoesNotExist:
        return Response({"Message": "Collection Request Not Found."}, status=status.HTTP_404_NOT_FOUND)


# End Of PUT Request Methods
