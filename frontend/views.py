import requests
from django.shortcuts import render
from django.http import HttpResponseServerError

# Create your views here.

base = "http://192.168.8.110:8000"


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
    context = {'collection': details}
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
    context = {'details': details}
    print(details)
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
