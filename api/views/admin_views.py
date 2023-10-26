import json
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import Collection, Waste,  Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer,RequestSerializer, RatingSerializer, CollectionSerializer


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

# Get All Requests
@api_view(['GET'])
def getRequests(request):
    requests = Requests.objects.all()
    serializer = RequestSerializer(requests, many=True)
    return Response(serializer.data) 


# Get Driver Rating
@api_view(['GET'])
def getDriverRating(request, collector_id):
    rating = Ratings.objects.filter(collector_id=collector_id)
    serializer = RatingSerializer(rating, many=True)
    return Response(serializer.data) 

# Get Cancelled Requests
@api_view(['GET'])
def getCancelledRequests(request):
    cancelled = Requests.objects.filter(request_status='Cancelled')
    serializer = RequestSerializer(cancelled, many=True)
    return Response(serializer.data)
    


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



# Add Waste Type
@api_view(['POST'])
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# Create User Account
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