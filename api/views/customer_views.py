import json
import logging
from django.conf import settings
from rest_framework import status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from base.models import CollectorProfile, CustomerProfile, Collection, Waste, Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, UserSerializer, RequestSerializer, CollectionSerializer, CollectorProfileSerializer, CustomerProfileSerializer, CustomerProfilesSerializer, CompletedCollectionSerializer


logger = logging.getLogger(__name__)


# GET Request Methods


# Get Waste Types


@api_view(['GET'])
def getWaste(request):
    waste = Waste.objects.all()
    serializer = WasteSerializer(waste, many=True)
    return Response(serializer.data) 


# Get Collector Details


@api_view(['GET'])
def view_collector_profile(request, collector_id):
    try:
        collector = CollectorProfile.objects.get(pk=collector_id)
    except CollectorProfile.DoesNotExist:
        return Response({'Message': 'Collector Profile Not Found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CollectorProfileSerializer(collector)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Get Collection Details


@api_view(['GET'])
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, request_id=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


# Get Customer Profile


@api_view(['GET'])
def getCustomerProfile(request, pk):
    profile = get_object_or_404(CustomerProfile, pk=pk)
    serializer = CustomerProfileSerializer(profile)
    return Response(serializer.data)


# Get all Customer Profiles


@api_view(['GET'])
def getCustomerProfiles(request):
    profiles = CustomerProfile.objects.all()
    serializer = CustomerProfilesSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def completed_collections_by_customer(request, customer_id):
    try:
        collections = Collection.objects.filter(request__customer_id=customer_id, request__request_status='Complete')
        serializer = CompletedCollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        return Response({"Message": "Completed Collections Not Found For This Customer."}, status=status.HTTP_404_NOT_FOUND)

# End of GET Request Methods



# POST Request Methods


@api_view(['POST'])
def add_collection_request(request):
    if request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Customer Record


@api_view(['POST'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(pk=pk)
    serializer = CustomerProfileSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#  Create User and Profile


@api_view(['POST'])
def create_user_and_profile(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            address = request.data.get('address')
            profile_data = {'address': address, 'auth': user_instance}
            profile_serializer = CustomerProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                
                # Sending email notification to the user
                subject = 'Account Creation Notification'
                message = 'Your eWaste Account Has Been Successfully Created.'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user_instance.email]
                send_mail(subject, message, from_email, to_email, fail_silently=True)
                
                return Response({'Message': 'User and Profile Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                user_instance.delete()
                return Response({'Error': 'Profile Creation Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add Customer Collection Request

@api_view(['POST'])
def create_request(request):
    if request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Cancel a Collection Request


@api_view(['POST']) 
def cancel_request(request, request_id):
    request_obj = get_object_or_404(Requests, pk=request_id)
    if request.user != request_obj.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
    request_obj.request_status = 'Cancelled'
    request_obj.save()
    return Response({'Message': 'Request Cancelled Successfully'}, status=status.HTTP_200_OK)


# Add Rating

@api_view(['POST'])
def add_rating(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    if request.user != collection.request.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
    rating_score = request.data.get('rating_score')
    if rating_score is None:
        return Response({'Message': 'Rating Score is Required'}, status=status.HTTP_400_BAD_REQUEST)
    rating = Ratings.objects.create(rating_score=rating_score, collection=collection)
    return Response({'Message': 'Rating Added Successfully'}, status=status.HTTP_201_CREATED)


# End of POST Request Methods


# PUT Method


# Update Customer Request Location

@api_view(['PUT'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(pk=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


