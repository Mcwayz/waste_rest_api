import requests
import datetime as date_time
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from base.models import Collection



# Create your views here.

base = "http://127.0.0.1:8000"


def dashboard(request):

    return render(request, 'frontend/dashboard.html',)


def index(request):
    return render(request, 'frontend/index.html')


def addType(request):
    return render(request, 'frontend/waste/add_type.html')


def WasteType(request):
    
    return render(request, 'frontend/waste/waste_type.html')

def users(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)


def collections(request):

    return render(request, 'frontend/collections.html')


def collection_requests(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/collection-requests")
    data = response.json()
    for item in data:
        request_date = date_time.datetime.strptime(item['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        user_collect_date = date_time.datetime.strptime(item['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['assigned_date'] = request_date
        item['user_collect_date'] = user_collect_date
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collection-requests.html', context)



def collection_details(request, pk):
    # Make a request to the endpoint to retrieve data
    api_url = f"{base}/api/collection-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    request_date = date_time.datetime.strptime(details['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    user_collect_date = date_time.datetime.strptime(details['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'collection': details, 'request_date': request_date, 'user_collect_date':user_collect_date}
    print(details)
    return render(request, 'frontend/collection_details.html', context)



def collection_summary(request, pk):
    # Make a request to the endpoint to retrieve data
    api_url = f"{base}/api/collection-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    request_date = date_time.datetime.strptime(details['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    user_collect_date = date_time.datetime.strptime(details['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'collection': details, 'request_date': request_date, 'user_collect_date':user_collect_date}
    print(details)
    return render(request, 'frontend/collection_summary.html', context)



def map_view(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    return render(request, 'frontend/map.html', {'latitude': latitude, 'longitude': longitude})


def add_user(request):
    return render(request, 'frontend/add-user.html')


