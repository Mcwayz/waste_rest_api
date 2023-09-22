import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import CustomerProfile, Collection, Waste, CollectorProfile, Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, CustomerSerializer, CollectorSerializer, UserSerializer, RequestSerializer, RatingSerializer, CollectionSerializer, CustomerLocationSerializer


#                            #
#                            #
#                            #
#    GET Request Methods     #
#                            #
#                            #
#                            #



@api_view(['GET'])
def getCollections(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data) 
  

# Get All Completed Collections
@api_view(['GET'])
def getCollected(request):
    collections = Collection.objects.filter(is_collected=True)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


# Get All Collectors
@api_view(['GET'])
def getCollectors(request):
    collectors = CollectorProfile.objects.all()
    serializer = CollectorSerializer(collectors, many=True)
    return Response(serializer.data) 


# Get All Customers
@api_view(['GET'])
def getCustomers(request):
    customers = CustomerProfile.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data) 


# Get Collection Details
@api_view(['GET'])
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


# Get Waste Type Details
@api_view(['GET'])
def wasteDetails(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    serializier = WasteSerializer(waste)
    return Response(serializier.data)


#                            #
#                            #
#                            #
# End Of GET Request Methods #
#                            #
#                            #
#                            # 






#                            #
#                            #
#                            #
#   POST Request Methods     #
#                            #
#                            #
#                            #




@api_view(['POST'])
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#                            #
#                            #
#                            #
#     End Of POST Methods    #
#                            #
#                            #
#                            # 
    



#                            #
#                            #
#                            #
#    PUT Request Methods     #
#                            #
#                            #
#                            #


@api_view(['PUT'])
def updateWaste(request, pk):
    waste = Waste.objects.get(waste_id=pk)
    serializer = WasteSerializer(instance=waste,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
#                            #
#                            #
#                            #
# End Of PUT Request Methods #
#                            #
#                            #
#                            # 



#                            #
#                            #
#                            #
#   DELETE Request Methods   #
#                            #
#                            #
#                            #

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the authenticated user has permission to delete this user
    if not request.user.is_superuser:
        return Response({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    user.delete()
    return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


#                            #
#                            #
#                            #
# DELETE Request Methods END #
#                            #
#                            #
#                            #