import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from ..utills.utills import get_collectors_within_radius
from base.models import CustomerProfile, Collection, Waste,Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, CustomerSerializer, CollectorSerializer, UserSerializer, RequestSerializer, CollectionSerializer, CustomerLocationSerializer


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

# Get Customer Profile
@api_view(['GET'])
def getCustomerProfile(request, pk):
    profile = get_object_or_404(CustomerProfile, pk=pk)
    serializer = CustomerSerializer(profile)
    return Response(serializer.data)


# Get Customers

@api_view(['GET'])
def getCustomerProfiles(request):
    profile = CustomerProfile.objects.all()
    serializer = CustomerSerializer(profile, many=True)
    return Response(serializer.data)


#                            #
#                            #
#                            #
#   GET Request Ends Here    #
#                            #
#                            #
#                            #



# Customer to view available Collectors within the area.
@api_view(['POST'])
def viewAvailableDrivers(request):
    serializer = CustomerLocationSerializer(data=request.data)
    
    if serializer.is_valid():
        latitude = str(serializer.validated_data['latitude'])  # Convert to string
        longitude = str(serializer.validated_data['longitude'])  # Convert to string
        
        # Query available collectors within a radius (e.g., 10 kilometers)
        collectors = get_collectors_within_radius(latitude, longitude, radius_km=10)
        
        # Serialize the collector profiles
        collector_data = CollectorSerializer(collectors, many=True).data
        
        return Response(collector_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Update Customer Record
@api_view(['POST'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(user_id=pk)
    serializer = CustomerSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Create Customer Account
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
        user.password1 = data['password1']
        user.password2 = data['password2']
        user.save()
        return Response({'Success': True, 'User_id': user.id}, status=status.HTTP_201_CREATED)
    else:
        return Response({'Success': False, 'Errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
# Add Customer Profile

@api_view(['POST'])
def addProfile(request):
    if request.method == 'POST':
        auth_id = request.data.get('auth_id')
        serializer = CollectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response({'Success': True, 'Auth_ID': auth_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Cancelling a Collection REquest
@api_view(['POST']) 
def cancel_request(request, request_id):
    try:
        request_obj = Requests.objects.get(pk=request_id)
    except Requests.DoesNotExist:
        return Response({'Message': 'Request Not Found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the authenticated user has permission to cancel this request
    if request.user != request_obj.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

    # You may want to add additional checks or business logic here
    # For example, you might want to check if the request can be canceled

    # Perform the cancellation logic here (e.g., update the request status)
    request_obj.request_status = 'Cancelled'
    request_obj.save()

    return Response({'Message': 'Request Cancelled Successfully'}, status=status.HTTP_200_OK)


# Add Rating
@api_view(['POST'])
def add_rating(request, collection_id):
    try:
        collection = Collection.objects.get(pk=collection_id)
    except Collection.DoesNotExist:
        return Response({'Message': 'Collection Not Found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the authenticated user is the customer who made the request
    if request.user != collection.request.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)

    # You can add additional validation logic for the rating data here
    # For example, validate that the rating score is within a certain range

    rating_score = request.data.get('rating_score')
    if rating_score is None:
        return Response({'mMssage': 'Rating Score is Required'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new rating object and associate it with the collection
    rating = Ratings.objects.create(rating_score=rating_score, collection=collection)

    return Response({'message': 'Rating Added Successfully'}, status=status.HTTP_201_CREATED)

    


#                            #
#                            #
#                            #
# End - POST Request Methods #
#                            #
#                            #
#                            # 
    
    
# ---------PUT Method--------#
    
    
    
# Update Customer Request Location 
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


# Update Customer Request Location
@api_view(['PUT'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(user_id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



    
