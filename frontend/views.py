import requests
import datetime as date_time
from .forms import WasteForm
from django.urls import reverse
from rest_framework.response import Response
from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404
from base.models import Waste, Collection, Wallet, CustomerProfile, CollectorProfile


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



# Get Customers List 


def list_customers(request):
    customers = CustomerProfile.objects.all()
    customer_data = []
    for customer in customers:
        customer_info = {
            "user_id": customer.auth.id,
            "username": customer.auth.username,
            "email": customer.auth.email,
            "first_name": customer.auth.first_name,
            "last_name": customer.auth.last_name,
            "address": customer.address
        }
        customer_data.append(customer_info)
    return render(request, 'frontend/customers/customers.html', {'customer_data': customer_data})


# Collectors List 


def list_collectors(request):
    collectors = CollectorProfile.objects.all()
    collectors_data = []
    for collector in collectors:
        collector_data = {
            'user_id': collector.auth.id,
            'username': collector.auth.username,
            'first_name': collector.auth.first_name,
            'last_name': collector.auth.last_name,
            'email': collector.auth.email,
            'waste_type': collector.waste.waste_type,
            'vehicle': collector.vehicle,
            'work_area': collector.work_area
        }
        collectors_data.append(collector_data)
    return render(request, 'frontend/collectors/collectors.html', {'collectors_data': collectors_data})


# Get Customer Details


def view_customer(request, user_id):
    customer = get_object_or_404(CustomerProfile, auth__id=user_id)
    customer_data = {
        'user_id': customer.auth.id,
        'username': customer.auth.username,
        'first_name': customer.auth.first_name,
        'last_name': customer.auth.last_name,
        'email': customer.auth.email,
        'address': customer.address
    }
    return render(request, 'frontend/customers/view_customer.html', {'customer_data': customer_data})


# Get Collector Details


def view_collector(request, user_id):
    collector =  get_object_or_404(CollectorProfile, auth__id=user_id)
    collector_data = {
        'user_id': collector.auth.id,
        'username': collector.auth.username,
        'first_name': collector.auth.first_name,
        'last_name': collector.auth.last_name,
        'email': collector.auth.email,
        'waste_type': collector.waste.waste_type,
        'vehicle': collector.vehicle,
        'work_area': collector.work_area
    }
    return render(request, 'frontend/collectors/view_collector.html', {'collector_data': collector_data})


def delete_collector(request, user_id):
    collector_data = get_object_or_404(CollectorProfile, auth__id=user_id)
    if request.method == 'POST':
        collector_data.delete()
        return redirect('Collectors') 
    return render(request, 'frontend/collectors/delete_collector.html', {'collector_data': collector_data})