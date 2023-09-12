import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from base.models import Subscription, Collection, Waste, UserProfile, TaskAssignment, Collectors
from .serializers import CollectorDetailsSerializer, SubSerializer, WasteSerializer, CollectionSerializer, UserSerializer, ProfileSerializer, CollectSerializer, SubscriptionSerializer, DetailsSerializer, CollectorSerializer, TaskAssignmentSerializer,TasksSerializer


#                            #
#                            #
#                            #
#    GET Request Methods     #
#                            #
#                            #
#                            #


@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'Waste Types' : '/waste-types/',
        'Collections' : '/collections/',
        'Subscriptions' : '/subscriptions/',
    }
    return Response(api_urls)


@api_view(['GET'])
def getSubscription(request):
    sub = Subscription.objects.select_related('user', 'waste').all()
    serializer = SubSerializer(sub, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def subscriptionDetails(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    serializer = SubSerializer(subscription)
    return Response(serializer.data)


@api_view(['GET'])
def getWaste(request):
    waste = Waste.objects.all()
    serializer = WasteSerializer(waste, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def wasteDetails(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    serializier = WasteSerializer(waste)
    return Response(serializier.data)


@api_view(['GET'])
def getCollections(request):
    collections = Collection.objects.filter(is_collected=False)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def getTasks(request):
    tasks = TaskAssignment.objects.filter(date_closed=None)
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMyTasks(request, auth_id):
    tasks = TaskAssignment.objects.filter(user=auth_id)
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCollected(request):
    collections = Collection.objects.filter(is_collected=True)
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


@api_view(['GET'])
def mySubs(request, auth_id):
    subscriptions = Subscription.objects.filter(user_id=auth_id)
    serializer = SubSerializer(subscriptions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCollectors(request):
    users = Collectors.objects.all()
    serializer = CollectorDetailsSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    users = get_object_or_404(UserProfile, pk=pk)
    serializer = UserSerializer(users)
    return Response(serializer.data)


@api_view(['GET'])
def getUserDetails(request, auth_id):
    user = get_object_or_404(UserProfile, auth__id=auth_id)
    serializer = DetailsSerializer(user)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
def getCollector(request, pk):
    users = get_object_or_404(Collectors, pk=pk)
    serializer = CollectorSerializer(users)
    return Response(serializer.data)


@api_view(['GET'])
def getCollectorDetails(request, auth_id):
    user = get_object_or_404(Collectors, auth__id=auth_id)
    serializer = DetailsSerializer(user)
    data = serializer.data
    return Response(data)


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
#    POST Request Methods    #
#                            #
#                            #
#                            #


@api_view(['POST'])
def addProfile(request):
    if request.method == 'POST':
        auth_id = request.data.get('auth_id')
        try:
            user = User.objects.get(id=auth_id)
        except User.DoesNotExist:
            return Response({'message': 'User Not Found'}, status=404)
        
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(auth=user)
            return Response({'success': True, 'auth_id': auth_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    return Response({'message': 'Invalid Request Method'}, status=405)


@api_view(['POST'])

def updateUser(request, pk):
    user = UserProfile.objects.get(user_id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])

def addCollection(request):
    serializer = CollectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def addCollector(request):
    serializer = CollectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updateWaste(request, pk):
    waste = Waste.objects.get(waste_id=pk)
    serializer = WasteSerializer(instance=waste,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def addSubscription(request):
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def updateSubscription(request, pk):
    sub = Subscription.objects.get(sub_id=pk)
    serializer = SubSerializer(instance=sub,data=request.data)
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
        user.password1 = data['password1']
        user.password2 = data['password2']
        user.save()
        return Response({'success': True, 'user_id': user.id}, status=status.HTTP_201_CREATED)
    else:
        return Response({'success': False, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def addAssignment(request):
    serializer = TaskAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

#                            #
#                            #
#                            #
# End - POST Request Methods #
#                            #
#                            #
#                            # 
    
    
# ------------PUT Method------------#
    
@api_view(['PUT'])
def update_collection(request, pk):
    collection = Collection.objects.get(pk=pk)
    collection.is_collected = True
    collection.collection_date = datetime.now()
    collection.save()

    # Update TaskAssignment
    
    task_assignment = TaskAssignment.objects.filter(collection=collection)
    task_assignment.update(date_closed=datetime.now())

    serializer = CollectionSerializer(collection)
    return Response(serializer.data)

# ------------End - Here--------------#