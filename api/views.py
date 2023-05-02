import json
from datetime import datetime
from rest_framework import status
from .serializers import SubSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from base.models import Subscription, Collection, Waste, UserProfile
from .serializers import SubSerializer, WasteSerializer, CollectionSerializer, UserSerializer, ProfileSerializer



@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'Users List' : '/users/',
        'Add Profile' : '/add-profile/',
        'Waste Types' : '/waste-types/',
        'Collections' : '/collections/',
        'Collections' : '/collections/',
        'Subscriptions' : '/subscriptions/',
        'Add Waste Type' : '/add-wastetype/',
        'Add Collection' : '/add-collection/',
        'Add Subscription' : '/add-subscription/',
        'Update Waste Type' : '/update-wastetype/',
        'Update Collection' : '/update-collection/',
        'Update Subscription' : '/update-subscription/',
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
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
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
def getUsers(request):
    users = UserProfile.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    users = get_object_or_404(UserProfile, pk=pk)
    serializer = UserSerializer(users)
    return Response(serializer.data)


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


@api_view(['POST'])
def addCollection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_collection(request, pk):
    collection = Collection.objects.get(pk=pk)
    collection.is_collected = request.data.get('is_collected', collection.is_collected)
    collection.collection_date = datetime.now()
    collection.save()
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


@api_view(['POST'])
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateWaste(request, pk):
    waste = Waste.objects.get(waste_id=pk)
    serializer = WasteSerializer(instance=waste,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addSubscription(request):
    serializer = SubSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateSubscription(request, pk):
    sub = Subscription.objects.get(sub_id=pk)
    serializer = SubSerializer(instance=sub,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


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