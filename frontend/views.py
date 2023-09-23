import requests
import datetime as date_time
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render
from base.models import Collection
from .decorators import token_required



# Create your views here.

base = "http://127.0.0.1:8000"


def dashboard(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/subscriptions")
    data = response.json()
 # Calculate the date range for active subscriptions (less than 30 days)
    today = timezone.now().date()
    thirty_days_ago = today - date_time.timedelta(days=30)
    active_subscriptions_count = Collection.objects.filter(sub_date__gte=thirty_days_ago).count()
    all_subscriptions_count = Collection.objects.count()
    collection_requests_count = Collection.objects.filter(is_collected=False).count()
    complete_collections_count = Collection.objects.filter(is_collected=True).count()
    overdue_subscriptions_count = all_subscriptions_count - active_subscriptions_count
    for item in data:
        sub_date = date_time.datetime.strptime(item['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['sub_date'] = sub_date


    context = {
        'data': data, 
        'collection_requests_count': collection_requests_count,
        'complete_collections_count': complete_collections_count,
        'active_subscriptions_count': active_subscriptions_count,
        'overdue_subscriptions_count': overdue_subscriptions_count,
    }

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
    for item in data:
        request_date = date_time.datetime.strptime(item['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        user_collect_date = date_time.datetime.strptime(item['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        collection_date = date_time.datetime.strptime(item['collection_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['request_date'] = request_date
        item['user_collect_date'] = user_collect_date
        item['collection_date'] = collection_date
    context = {'data': data}
    print(data)
    return render(request, 'frontend/collections.html', context)


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


def task_assignments(request):
    # Make a request to the endpoint to retrieve data
    response = requests.get(f"{base}/api/tasks")
    data = response.json()
    for item in data:
        assigned_date = date_time.datetime.strptime(item['assigned_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['assigned_date'] = assigned_date
    context = {'data': data}
    print(data)
    return render(request, 'frontend/assignment-tasks.html', context)


def task_details(request, pk):
    # Make a request to the endpoint to retrieve data
    api_url = f"{base}/api/my-tasks/1/{pk}/"
    response = requests.get(api_url)
    details = response.json()
    request_date = date_time.datetime.strptime(details['request_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    assigned_date = date_time.datetime.strptime(details['assigned_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    user_collect_date = date_time.datetime.strptime(details['user_collect_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    context = {'collection': details, 'request_date': request_date, 'user_collect_date':user_collect_date, 'assigned_date':assigned_date}
    print(details)
    return render(request, 'frontend/assigned-task-details.html', context)


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
    
    for item in data:
        sub_date = date_time.datetime.strptime(item['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['sub_date'] = sub_date
    
    context = {'data': data}
    print(data)
    return render(request, 'frontend/subscriptions.html', context)


def sub_details(request, pk):
    api_url = f"{base}/api/subscription-details/{pk}"
    response = requests.get(api_url)
    details = response.json()
    sub_date = date_time.datetime.strptime(details['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    due_date = sub_date + timedelta(days=30)
    context = {'details': details, 'sub_date': sub_date, 'due_date': due_date}
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
    today = date_time.datetime.now().date()
    one_month_ago = today - timedelta(days=30)
    filtered_data = [sub for sub in data if date_time.datetime.strptime(sub['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ").date() <= one_month_ago]
    for item in filtered_data:
        sub_date = date_time.datetime.strptime(item['sub_date'], "%Y-%m-%dT%H:%M:%S.%fZ")
        item['sub_date'] = sub_date
    context = {'data': filtered_data}
    print(filtered_data)
    return render(request, 'frontend/overdue.html', context)
