import json
import logging
from rest_framework import status
from django.db import transaction
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from base.models import CollectorProfile, CustomerProfile, Collection, Waste, Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, UserSerializer, RequestSerializer, CollectionSerializer, CollectorProfileSerializer, CustomerProfileSerializer


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
    collection = get_object_or_404(Collection, pk=pk)
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
    serializer = CustomerProfileSerializer(profiles, many=True)
    return Response(serializer.data)


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



# Create the customer account 


@api_view(['POST'])
def create_customer_account(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        with transaction.atomic():
            try:
                user_instance = user_serializer.save()
            except IntegrityError as e:
                logger.error(f"IntegrityError: {e}")
                return Response({'Success': False, 'Errors': 'Username Already Exists.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # If user_instance is an integer, retrieve the User object
            if isinstance(user_instance, int):
                try:
                    user_instance = User.objects.get(id=user_instance)
                except User.DoesNotExist:
                    logger.error("User with provided ID Does Not Exist.")
                    return Response({'Success': False, 'Errors': 'Invalid User ID.'}, status=status.HTTP_400_BAD_REQUEST)
            
            auth_user = user_instance  # Use the User instance
            auth_user_id = auth_user.id
            
            logger.error(f"User ID: {auth_user_id}")
            profile_data = {'address': request.data.get('address'), 'auth': auth_user}
            profile_serializer = CustomerProfileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({'Success': True, 'User_ID': auth_user_id}, status=status.HTTP_201_CREATED)
            else:
                user_instance.delete()
                return Response({'Success': False, 'Errors': profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.error(f"user_serializer errors: {user_serializer.errors}")
        return Response({'Success': False, 'Errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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


    
    
'''
@api_view(['POST'])
def viewAvailableDrivers(request):
    try:
        data = request.data  # Get data from the request body
        latitude = float(data.get('latitude'))
        longitude = float(data.get('longitude'))
    except (ValueError, TypeError):
        return Response({"message": "Invalid latitude or longitude provided."}, status=400)     

    # Define the search radius in kilometers (15 kilometers)
    search_radius = 15.0

    # Convert latitude and longitude from degrees to radians
    customer_lat_rad = math.radians(latitude)
    customer_lon_rad = math.radians(longitude)

    # Query all collector profiles from the database
    collectors = CollectorProfile.objects.all()

    # Filter collectors within the specified radius
    collectors_within_radius = []

    for collector in collectors:
        collector_lat_rad = math.radians(collector.latitude)
        collector_lon_rad = math.radians(collector.longitude)

        # Haversine formula for distance calculation
        dlon = collector_lon_rad - customer_lon_rad
        dlat = collector_lat_rad - customer_lat_rad
        a = math.sin(dlat/2)**2 + math.cos(customer_lat_rad) * math.cos(collector_lat_rad) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance_km = 6371 * c  

        if distance_km <= search_radius:
            collectors_within_radius.append(collector)
    collector_data = CollectorProfileSerializer(collectors_within_radius, many=True).data

    return Response(collector_data, status=200)
'''
