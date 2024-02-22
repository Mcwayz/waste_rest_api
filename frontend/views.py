import requests
import datetime as date_time
from .forms import WasteForm
from rest_framework.response import Response
from base.models import Waste, Collection
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.

base = "http://127.0.0.1:8000"


def dashboard(request):

    return render(request, 'frontend/dashboard.html',)


def index(request):
    return render(request, 'frontend/index.html')


def addType(request):
    return render(request, 'frontend/waste/add_type.html')


# Create Waste Type

def create_waste(request):
    if request.method == 'POST':
        form = WasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Waste Type') + '?alert=success')
    else:
        form = WasteForm()
    return render(request, 'frontend/waste/add_type.html', {'form': form})


# Waste Type Route

def WasteType(request):
    waste_types = Waste.objects.all()
    return render(request, 'frontend/waste/waste_type.html', {'waste_types': waste_types})



# Completed Collections

def get_completed_collections(request):
    response = requests.get(f'{base}/api/completedCollections/')
    if response.status_code == 200:
        completed_collections = response.json()
        for collection in completed_collections:
            collection_date_str = collection['collection_date']
            collection_date = date_time.datetime.fromisoformat(collection_date_str)
            collection['collection_date'] = collection_date.strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'frontend/collections/collections.html', {'completed_collections': completed_collections})
    else:
        return render(request, 'frontend/collections/collections.html', {'Error_Message': 'Failed To Fetch Data From The Endpoint'})
    
    
    
# Completed Collection

def get_completed_collection(request, request_id):
    response = requests.get(f'{base}/api/completedCollection/{request_id}/')
    if response.status_code == 200:
        completed_collection = response.json()
        collection_date_str = completed_collection['collection_date']
        collection_date = date_time.datetime.fromisoformat(collection_date_str)
        completed_collection['collection_date'] = collection_date.strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'frontend/collections/view_collection.html', {'completed_collection': completed_collection})
    else:
        return render(request, 'frontend/collections/collections.html', {'Error_Message': 'Failed To Fetch Data From The Endpoint'})


# Edit Waste Type

def edit_waste(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    if request.method == 'POST':
        form = WasteForm(request.POST, instance=waste)
        if form.is_valid():
            form.save()
            return redirect('Waste Type')
    else:
        form = WasteForm(instance=waste)
    return render(request, 'frontend/waste/edit_waste.html', {'form': form, 'waste': waste})



#Delete Waste Type


def delete_waste(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    if request.method == 'POST':
        waste.delete()
        return redirect('Waste Type') 
    return render(request, 'frontend/waste/delete_waste.html', {'waste': waste})



def users(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)




    """
    
def collection_details(request, pk):

    api_url = f"{base}/api/collection-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    request_date = date_time.datetime.strptime(details['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    user_collect_date = date_time.datetime.strptime(details['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'collection': details, 'request_date': request_date, 'user_collect_date':user_collect_date}
    print(details)
    return render(request, 'frontend/collection_details.html', context)



def collection_summary(request, pk):
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

    """


