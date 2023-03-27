from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Subscription, Collection, Waste, User
from .serializers import SubSerializer, WasteSerializer, CollectionSerializer, UserSerializer

@api_view(['GET'])
def getSubscription(request):
    Sub  = Subscription.objects.all()
    serializer = SubSerializer(Sub, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def getWaste(request):
    waste = Waste.objects.all()
    serializer = WasteSerializer(waste, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def getCollections(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
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
def addWaste(request):
    serializer = WasteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addSubscription(request):
    serializer = SubSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

