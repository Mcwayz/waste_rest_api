import json
from datetime import datetime
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from base.models import CustomerProfile, Collection, Waste, CollectorProfile, Requests, Ratings
from ..serializers.customer_serializer import WasteSerializer, CustomerSerializer, CollectorSerializer, UserSerializer, RequestSerializer, RatingSerializer, CollectionSerializer


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



