import json
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import Collection, Waste, Requests, Ratings
from ..serializers.collector_serializer import  CompletedCollectionSerializer
from ..serializers.customer_serializer import WasteSerializer, RequestSerializer, RatingSerializer, CollectionSerializer


# GET Request Methods


# Get Completed Collections 


# Retrieves all completed collections


@api_view(['GET'])
def get_completed_collections(request):
    completed_collections = Collection.objects.filter(request__request_status='Complete')
    serializer = CompletedCollectionSerializer(completed_collections, many=True)
    return Response(serializer.data)


# Retrieves a specific completed collection by request ID


@api_view(['GET'])
def get_completed_collection(request, request_id):
    completed_collection = get_object_or_404(Collection, request_id=request_id, request__request_status='Complete')
    serializer = CompletedCollectionSerializer(completed_collection)
    return Response(serializer.data)


# Retrieves all collected items


@api_view(['GET'])
def getCollected(request):
    collections = Collection.objects.filter(is_collected=True)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)



# Retrieves details of a specific collection



@api_view(['GET'])
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


# Retrieves details of a specific waste item


@api_view(['GET'])
def wasteDetails(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    serializer = WasteSerializer(waste)
    return Response(serializer.data)



# Retrieves all requests


@api_view(['GET'])
def getRequests(request):
    requests = Requests.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data)


# Retrieves ratings of a specific driver (collector)


@api_view(['GET'])
def getDriverRating(request, collector_id):
    rating = Ratings.objects.filter(collector_id=collector_id)
    serializer = RatingSerializer(rating, many=True)
    return Response(serializer.data)


# Retrieves all cancelled requests


@api_view(['GET'])
def getCancelledRequests(request):
    cancelled = Requests.objects.filter(request_status='Cancelled')
    serializer = RequestSerializer(cancelled, many=True)
    return Response(serializer.data)


# End Of GET Request Methods


# POST Request Methods


@api_view(['POST'])
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_user(request):
    data = json.loads(request.body)
    form = UserCreationForm(data)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = data['username']
        user.email = data['email']
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.set_password(data['password1'])
        user.save()
        return Response({'Success': True, 'User_id': user.id}, status=status.HTTP_201_CREATED)
    else:
        return Response({'Success': False, 'Errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


# End Of POST Methods


# PUT Request Methods


@api_view(['PUT'])
def updateWaste(request, pk):
    waste = Waste.objects.get(waste_id=pk)
    serializer = WasteSerializer(instance=waste, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# End Of PUT Request Methods


# DELETE Request Methods

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'Message': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if not request.user.is_superuser:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

    user.delete()
    return Response({'Message': 'User Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)

# DELETE Request Methods END



# total_collections_per_month view

def total_collections_per_month(request):
    
    return Response()



