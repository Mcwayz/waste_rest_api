import requests
from django.shortcuts import render
from base.models import Subscription
# Create your views here.


def dashboard(request):
    response = requests.get("http://127.0.0.1:8000/api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/home.html', context)


def index(request):
    return render(request, 'frontend/index.html')


def users(request):
    response = requests.get("http://127.0.0.1:8000/api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)


def collections(request):
    response = requests.get("http://127.0.0.1:8000/api/collections")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collections.html', context)


def subscriptions(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get("http://127.0.0.1:8000/api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/subscriptions.html', context)


def sub_details(request, pk):
    details = subscriptions.objects.get(pk=pk)
    context = {'details': details}
    return render(request, 'frontend/sub_details.html', context)


def display_map(request):
    latitude = request.GET.get('latitude', None)
    longitude = request.GET.get('longitude', None)
    context = {'latitude': latitude, 'longitude': longitude}
    return render(request, 'frontend/collections.html', context)
