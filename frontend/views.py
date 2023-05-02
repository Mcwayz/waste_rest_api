import requests
from django.shortcuts import render
from base.models import Subscription
# Create your views here.

base = "http://192.168.88.81:8000/"


def dashboard(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/home.html', context)


def index(request):
    return render(request, 'frontend/index.html')


def users(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)


def collections(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/collections")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collections.html', context)


def collection_requests(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/collection-requests")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collection-requests.html', context)


def subscriptions(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/subscriptions.html', context)


def sub_details(request, pk):
    details = subscriptions.objects.get(pk=pk)
    context = {'details': details}
    return render(request, 'frontend/sub_details.html', context)


def map_view(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    return render(request, 'frontend/map.html', {'latitude': latitude, 'longitude': longitude})


def add_user(request):
    return render(request, 'frontend/add-user.html')


def overdue(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(base+"api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/overdue.html', context)