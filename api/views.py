from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Subscription, Collection, Waste, User
from .serializers import SubSerializer, WasteSerializer, CollectionSerializer, UserSerializer
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse


@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'Users List' : '/users/',
        'Add User' : '/add-user/',
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
    Sub  = Subscription.objects.all() 
    serializer = SubSerializer(Sub, many=True)
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
def collectionDetails(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    users = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(users)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateUser(request, pk):
    user = User.objects.get(user_id=pk)
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


@api_view(['POST'])
def updateCollection(request, pk):
    collection = Collection.objects.get(collection_id=pk)
    serializer = CollectionSerializer(instance=collection,data=request.data)
    if serializer.is_valid():
        serializer.save()
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