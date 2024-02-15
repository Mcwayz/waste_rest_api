import requests
import datetime as date_time
from .forms import WasteForm
from base.models import Waste
from django.urls import reverse
from django.shortcuts import render, redirect



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




# Edit Waste Type 

def edit_waste(request, pk):
    # Your view logic here
    return render(request, 'edit_waste.html', {'pk': pk})



# Delete Waste Type

def delete_waste(request, pk):
    # Your view logic here
    return render(request, 'delete_waste.html', {'pk': pk})




def users(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/users")
    data = response.json()
    context = {'data': data}
    return render(request, 'frontend/manage-users.html', context)


def collections(request):

    return render(request, 'frontend/collections.html')



    """
    
def collection_requests(request):

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


