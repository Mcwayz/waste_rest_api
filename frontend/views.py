import requests
import datetime
from django.shortcuts import render
from .decorators import token_required

# Create your views here.

base = "http://192.168.1.79:8000"


def dashboard(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/home.html', context)


def index(request):
    return render(request, 'frontend/index.html')


def users(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)


def collections(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/collections")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collections.html', context)


def collection_requests(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/collection-requests")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collection-requests.html', context)


def collection_details(request, pk):
    # Make a request to the endpoint to retrieve data
    api_url = f"{base}/api/collection-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    request_date = datetime.datetime.strptime(details['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'collection': details, 'request_date': request_date}
    print(details)
    return render(request, 'frontend/collection_details.html', context)


def update_collection(request, pk):
    # Make a request to the endpoint to retrieve data
    api_url = f"{base}/api/update-collection/{pk}/"
    response = requests.get(api_url)
    details = response.json()
    context = {'collection': details}
    print(details)
    return render(request, 'frontend/collection_details.html', context)


def subscriptions(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/subscriptions.html', context)


def sub_details(request, pk):
    api_url = f"{base}/api/subscription-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    sub_date = datetime.datetime.strptime(details['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'details': details, 'sub_date': sub_date}
    return render(request, 'frontend/sub_details.html', context)


def map_view(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    return render(request, 'frontend/map.html', {'latitude': latitude, 'longitude': longitude})


def add_user(request):
    return render(request, 'frontend/add-user.html')


def overdue(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/subscriptions")
    data = response.json()
    context = {'data': data}
    print(data)
    return render(request, 'frontend/overdue.html', context)
