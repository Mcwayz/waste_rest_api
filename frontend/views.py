import requests
import datetime as date_time
from .forms import WasteForm
from rest_framework.response import Response
from base.models import Waste, Collection, Wallet
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
    
    
    
# Pending Requests


def get_customer_requests(request):
    response = requests.get(f'{base}/api/customerRequests/')
    if response.status_code == 200:
        customer_requests = response.json()
        for request_data in customer_requests:
            request_date_str = request_data['request_date']
            # Parse the date string
            request_date = date_time.datetime.strptime(request_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
            # Format the date
            request_data['request_date'] = request_date.strftime('%Y-%m-%d %H:%M:%S')
        return render(request, 'frontend/collections/requests.html', {'customer_requests': customer_requests})
    else:
        return render(request, 'frontend/collections/requests.html', {'Error_Message': 'Failed To Fetch Data From The Endpoint'})



# Collector Wallets


def get_collector_wallets(request):
    response = requests.get(f'{base}/api/wallets/')
    if response.status_code == 200:
        collector_wallets = response.json()
        return render(request, 'frontend/wallet/wallets.html', {'collector_wallets': collector_wallets})
    else:
        return render(request, 'frontend/wallet/wallets.html', {'Error_Message': 'Failed To Fetch Data From The Endpoint'})
    

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


# Delete Waste Type


def delete_waste(request, pk):
    waste = get_object_or_404(Waste, pk=pk)
    if request.method == 'POST':
        waste.delete()
        return redirect('Waste Type') 
    return render(request, 'frontend/waste/delete_waste.html', {'waste': waste})





# View Wallet


def view_wallet(request, wallet_id):
    response = requests.get(f'{base}/api/view-wallet/{wallet_id}/')
    if response.status_code == 200:
        wallet = response.json()
        return render(request, 'frontend/wallet/view_wallet.html', {'wallet': wallet})
    else:
        return render(request, 'frontend/wallet/view_wallet.html', {'Error_Message': 'Failed To Fetch Data From The Endpoint'})


# Delete Collector Wallet


def delete_wallet(request, pk):
    wallet = get_object_or_404(Wallet, pk=pk)
    if request.method == 'POST':
        wallet.delete()
        return redirect('Waste Type') 
    return render(request, 'frontend/wallet/delete_wallet.html', {'wallet': wallet})