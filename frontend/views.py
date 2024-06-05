import logging
from datetime import datetime
from django.urls import reverse
from django.contrib import messages
from collections import defaultdict
from .forms import WasteForm, ChargeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout 
from django.shortcuts import render, redirect, get_object_or_404
from base.models import Waste, Collection, Wallet, CustomerProfile, CollectorProfile, Requests, WalletHistory, User, WasteGL, ServiceCharge, CollectorCommission


logger = logging.getLogger(__name__)

# Login view


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                auth_login(request, user)
                return redirect('Dash') 
            else:
                messages.error(request, 'Invalid email or password.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
    return render(request, 'frontend/auth/login.html')


# Logout View


def user_logout(request):
    logout(request)
    return redirect('login')


# Reset Password View


@login_required
def reset_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        user = request.user
        if not user.check_password(old_password):
            messages.error(request, 'Your old password is incorrect.')
        elif new_password != confirm_new_password:
            messages.error(request, 'New password and confirm password do not match.')
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('login') 

    return render(request, 'frontend/auth/reset-password.html')


# Views for the Profile

# Profile Information


def user_profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'frontend/profile/profile.html', context) 


# Update Profile Information 


def edit_profile_info(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update user information
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        # Display success message
        messages.success(request, 'Your information has been updated successfully.')

        # Redirect to profile page or any other page after updating
        return redirect('user_profile')  # Change 'user_profile' to the name of your profile view
    
    return render(request, 'frontend/profile/profile.html')


# Dashboard View


@login_required
def dashboard(request):
    # Query for system users
    user = request.user
    total_users = User.objects.count()
    total_requests_count = Requests.objects.count()
    total_requests = Requests.objects.exclude(request_status='complete').count()
    total_pending_requests = Requests.objects.filter(request_status='pending').count()
    total_complete_collections = Requests.objects.filter(request_status='complete').count()

    # Get all collections
    collections = Collection.objects.all()
    
    # Group collections by waste type and count the number of collections per waste type
    collections_by_waste_type = defaultdict(int)
    for collection in collections:
        waste_type = collection.request.waste.waste_type
        collections_by_waste_type[waste_type] += 1

    # Prepare data for the pie chart
    pie_chart_data = {
        'series': list(collections_by_waste_type.values()),
        'labels': list(collections_by_waste_type.keys()),
    }

    # Group collections by month and calculate total income for each month
    collections_by_month = defaultdict(float)
    for collection in collections:
        month_year = collection.collection_date.strftime("%Y-%m")
        collections_by_month[month_year] += float(collection.request.collection_price)

    # Group collections by waste type and calculate total income for each waste type
    collections_by_waste = defaultdict(float)
    for collection in collections:
        waste_type = collection.request.waste.waste_type
        collections_by_waste[waste_type] += float(collection.request.collection_price)

    # Prepare data for the JavaScript function
    month_names = [] 
    total_income_by_month = []
    for month_year, total_income in collections_by_month.items():
        month_names.append(datetime.strptime(month_year, "%Y-%m").strftime("%b %Y"))
        total_income_by_month.append(total_income)

    # Prepare waste data with zero income for waste types with no collections
    waste_data = []
    all_waste_types = set(Waste.objects.values_list('waste_type', flat=True))
    for waste_type in all_waste_types:
        total_income = collections_by_waste.get(waste_type, 0)
        waste_data.append({
            'waste_type': waste_type,
            'total_income': total_income,
            'change': ' Real-Time Data'
        })

    # Get recent collections data
    recent_collections = Collection.objects.order_by('-collection_date')[:5]

    # Prepare recent collections data for rendering

    recent_collections_data = []
    for collection in recent_collections:
        recent_collections_data.append({
            'customer_initials': collection.request.customer.auth.first_name[0] + collection.request.customer.auth.last_name[0],
            'customer_name': collection.request.customer.auth.get_full_name(),
            'waste_type': collection.request.waste.waste_type,
            'amount': collection.request.collection_price,
            'collection_date': collection.collection_date
        })

        
    # Calculate the percentage of requests
    percentage_of_total_requests = round((total_requests / total_requests_count) * 100, 1) if total_requests_count > 0 else 0
    percentage_of_pending_requests = round((total_pending_requests / total_requests_count) * 100, 1) if total_requests_count > 0 else 0
    percentage_of_complete_requests = round((total_complete_collections / total_requests_count) * 100, 1) if total_requests_count > 0 else 0


    context = {
        'user': user,
        'js_data': {
            'income_data': total_income_by_month,
            'categories': month_names,
        },
        'waste_data': waste_data,
        'total_users': total_users,
        'total_requests': total_requests,
        'pie_chart_data': pie_chart_data,
        'recent_collections': recent_collections_data,
        'total_pending_requests': total_pending_requests,
        'total_complete_collections': total_complete_collections,
        'percentage_of_total_requests': percentage_of_total_requests,
        'percentage_of_pending_requests': percentage_of_pending_requests,
        'percentage_of_complete_requests': percentage_of_complete_requests,
    }
    return render(request, 'frontend/base/dashboard.html', context)



def index(request):
    return render(request, 'frontend/base/landing.html')


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


# Create Service Configs

def add_service(request):
    if request.method == 'POST':
        form = ChargeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Service Configs') + '?alert=success')
    else:
        form = ChargeForm()
    return render(request, 'frontend/waste/service_charge.html', {'form': form})

# Service Configs


def ServiceConfigs(request):
    service_charge = ServiceCharge.objects.all()
    return render(request, 'frontend/waste/service_charge.html', {'service_charge': service_charge})



# Edit Service Charge Type


def edit_charge(request, pk):
    service = get_object_or_404(ServiceCharge, pk=pk)
    if request.method == 'POST':
        form = ChargeForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('Service Configs')
    else:
        form = ChargeForm(instance=service)
    return render(request, 'frontend/waste/edit_charge.html', {'form': form, 'service': service})


# Delete Service Type


def delete_service(request, pk):
    service = get_object_or_404(ServiceCharge, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('Service Configs') 
    return render(request, 'frontend/waste/delete_config.html', {'service': service})


# Completed Collections


def get_completed_collections(request):
    collection_data = Collection.objects.filter(request__request_status='Complete')

    completed_collections = []
    for collection_obj in collection_data:
        request_obj = collection_obj.request
        customer_name = f"{request_obj.customer.auth.first_name} {request_obj.customer.auth.last_name}"
        collector_name = f"{collection_obj.collector.auth.first_name} {collection_obj.collector.auth.last_name}"

        collection_info = {
            "request_id": request_obj.request_id,
            "location": request_obj.location,
            "request_status": request_obj.request_status,
            "request_date": request_obj.request_date,
            "collection_date": collection_obj.collection_date,
            "collection_price": str(request_obj.collection_price),
            "waste": request_obj.waste.waste_type,
            "customer_name": customer_name.strip(),
            "collector_name": collector_name.strip()
        }
        completed_collections.append(collection_info)

    return render(request, 'frontend/collections/collections.html', {'completed_collections': completed_collections})
    
    
    
# Completed Collection


def get_completed_collection(request, request_id):
    collection_data = get_object_or_404(Collection, request_id=request_id)
    completed_collection = {
        "request_id": collection_data.request_id,
        "location": collection_data.request.location,
        "request_status": collection_data.request.request_status,
        "request_date": collection_data.request.request_date,
        "collection_date": collection_data.collection_date,
        "collection_price": str(collection_data.request.collection_price),
        "waste": collection_data.request.waste.waste_type,
        "customer_name": collection_data.request.customer.auth.first_name + " " + collection_data.request.customer.auth.last_name,
        "collector_name": collection_data.collector.auth.first_name + " " + collection_data.collector.auth.last_name
    }

    return render(request, 'frontend/collections/view_collection.html', {'completed_collection': completed_collection})
    
    
    
# Pending Requests


def get_customer_requests(request):
    requests = Requests.objects.filter(request_status='Pending')
    customer_requests = []
    for request_obj in requests: 
        full_name = f"{request_obj.customer.auth.first_name} {request_obj.customer.auth.last_name}"

        request_data = {
            "request_id": request_obj.request_id,
            "location": request_obj.location,
            "number_of_bags": request_obj.number_of_bags,
            "request_status": request_obj.request_status,
            "request_date": request_obj.request_date,
            "collection_price": str(request_obj.collection_price),
            "waste": request_obj.waste.waste_type,
            "customer": full_name
        }
        customer_requests.append(request_data)
    return render(request, 'frontend/collections/requests.html', {'customer_requests': customer_requests})


# Collector Wallets


def get_collector_wallets(request):
    wallets = Wallet.objects.all()
    collector_wallets = []
    for wallet in wallets:
        collector_data = {
            "wallet_id": wallet.wallet_id,
            "first_name": wallet.collector.auth.first_name,
            "last_name": wallet.collector.auth.last_name,
            "vehicle": wallet.collector.vehicle,
            "work_area": wallet.collector.work_area,
            "waste": wallet.collector.waste.waste_type,
            "wallet_balance": str(wallet.balance)
        }
        collector_wallets.append(collector_data)
    return render(request, 'frontend/wallet/wallets.html', {'collector_wallets': collector_wallets})
    

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
    wallet = get_object_or_404(Wallet, wallet_id=wallet_id)
    
    # Get wallet data
    wallet_data = {
        "wallet_id": wallet.wallet_id,
        "first_name": wallet.collector.auth.first_name,
        "last_name": wallet.collector.auth.last_name,
        "vehicle": wallet.collector.vehicle,
        "work_area": wallet.collector.work_area,
        "waste": wallet.collector.waste.waste_type,
        "wallet_balance": str(wallet.balance)
    }
    
    # Get wallet history
    wallet_history = WalletHistory.objects.filter(wallet=wallet)
    
    # Pass wallet and wallet history data to the template
    return render(request, 'frontend/wallet/view_wallet.html', {'wallet': wallet_data, 'wallet_history': wallet_history})


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
            'vehicle': collector.vehicle,
            'user_id': collector.auth.id,
            'email': collector.auth.email,
            'work_area': collector.work_area,
            'username': collector.auth.username,
            'last_name': collector.auth.last_name,
            'collector_id': collector.collector_id,
            'first_name': collector.auth.first_name,
            'waste_type': collector.waste.waste_type
        }
        logger.error(f"Collector Data: {collector_data}")
        
        collectors_data.append(collector_data)
    return render(request, 'frontend/collectors/collectors.html', {'collectors_data': collectors_data})



def general_ledger(request):
    ledger = WasteGL.objects.all()
    total_value = 0
    waste_gl = []
    for waste_ledger in ledger:
        total_value = waste_ledger.new_GL_balance
        transaction_amount  = waste_ledger.new_GL_balance - waste_ledger.old_GL_balance
        entry = {
            'gl_id': waste_ledger.gl_id,
            'extras': waste_ledger.extras,
            'transaction_amount': transaction_amount,
            'old_GL_balance': waste_ledger.old_GL_balance,
            'new_GL_balance': waste_ledger.new_GL_balance,
            'service_charge': waste_ledger.service_charge,
            'transaction_type': waste_ledger.transaction_type,
            'transaction_date': waste_ledger.transaction_date,
            'collection_id': waste_ledger.collection.collection_id
        }
        
        # Append the dictionary to the list of ledger entries
        waste_gl.append(entry)
    # Pass the list of ledger entries and total value to the template
    return render(request, 'frontend/wallet/general_ledger.html', {'waste_gl': waste_gl, 'total_value': total_value})



# Commissions Data 


def list_commission(request, collector_id):
    total_value = 0
    commissions_data = []
    commissions = CollectorCommission.objects.filter(collector_id=collector_id)
    for commission in commissions:
        commission_data = {
            'comment': commission.extras,
            'commission_id': commission.txn_id,
            'commission': commission.commission,
            'commission_settlement_date': commission.commission_settlement_date
        }
        commissions_data.append(commission_data)
        total_value += commission.commission
    return render(request, 'frontend/collectors/commission.html', {'commissions_data': commissions_data, 'total_value': total_value})


# Get Customer Details


def view_customer(request, user_id):
    customer = get_object_or_404(CustomerProfile, auth__id=user_id)
    customer_data = {
        'user_id': customer.auth.id,
        'address': customer.address,
        'email': customer.auth.email,
        'username': customer.auth.username,
        'last_name': customer.auth.last_name,
        'first_name': customer.auth.first_name,
    }
    return render(request, 'frontend/customers/view_customer.html', {'customer_data': customer_data})


# Get Collector Details


def view_collector(request, user_id):
    collector =  get_object_or_404(CollectorProfile, auth__id=user_id)
    collector_data = {
        'vehicle': collector.vehicle,
        'user_id': collector.auth.id,
        'email': collector.auth.email,
        'work_area': collector.work_area,
        'username': collector.auth.username,
        'last_name': collector.auth.last_name,
        'collector_id': collector.collector_id,
        'first_name': collector.auth.first_name,
        'waste_type': collector.waste.waste_type
        
    }
    return render(request, 'frontend/collectors/view_collector.html', {'collector_data': collector_data})



# Delete Collector Profile


def delete_collector(request, user_id):
    collector = get_object_or_404(CollectorProfile, auth__id=user_id)
    collector_data = {
        'vehicle': collector.vehicle,
        'user_id': collector.auth.id,
        'email': collector.auth.email,
        'work_area': collector.work_area,
        'username': collector.auth.username,
        'last_name': collector.auth.last_name,
        'collector_id': collector.collector_id,
        'first_name': collector.auth.first_name,
        'waste_type': collector.waste.waste_type
    }
    if request.method == 'POST':
        collector_data.delete()
        return redirect('Collectors') 
    return render(request, 'frontend/collectors/delete_collector.html', {'collector_data': collector_data})


# General Ledger

def general_ledger(request):
    ledger = WasteGL.objects.all()
    total_value = 0
    waste_gl = []
    for waste_ledger in ledger:
        total_value = waste_ledger.new_GL_balance
        transaction_amount  = waste_ledger.new_GL_balance - waste_ledger.old_GL_balance
        entry = {
            'gl_id': waste_ledger.gl_id,
            'extras': waste_ledger.extras,
            'transaction_amount': transaction_amount,
            'old_GL_balance': waste_ledger.old_GL_balance,
            'new_GL_balance': waste_ledger.new_GL_balance,
            'service_charge': waste_ledger.service_charge,
            'transaction_type': waste_ledger.transaction_type,
            'transaction_date': waste_ledger.transaction_date,
            'collection_id': waste_ledger.collection.collection_id
        }
        
        # Append the dictionary to the list of ledger entries
        waste_gl.append(entry)
    # Pass the list of ledger entries and total value to the template
    return render(request, 'frontend/wallet/general_ledger.html', {'waste_gl': waste_gl, 'total_value': total_value})