from . import views
from django.urls import path
from .decorators.security import superuser_required

urlpatterns = [
    # URL accessible to all users
    path('', views.dashboard, name='Index'),
    # URLs accessible only to authenticated super-users
    path('dashboard/', superuser_required(views.dashboard), name='Dash'),
    path('add-type/', superuser_required(views.addType), name='Add Type'),
    path('home/', superuser_required(views.dashboard), name='Admin Dashboard'),
    path('waste-type/', superuser_required(views.WasteType), name='Waste Type'),
    path('customers/', superuser_required(views.list_customers), name='Customers'),
    path('collectors/', superuser_required(views.list_collectors), name='Collectors'),
    path('add-waste-type/', superuser_required(views.create_waste), name='Add WasteType'),
    path('wallet/<int:wallet_id>/', superuser_required(views.view_wallet), name='view_wallet'),
    path('wallets/', superuser_required(views.get_collector_wallets), name='Collector Wallets'), 
    path('requests/', superuser_required(views.get_customer_requests), name='Pending Requests'),
    path('edit-waste-type/<int:pk>/', superuser_required(views.edit_waste), name='edit_waste'),
    path('delete-waste/<int:pk>/', superuser_required(views.delete_waste), name='delete_waste'),
    path('collections/', superuser_required(views.get_completed_collections), name='Collections'),
    path('delete-wallet/<int:pk>/', superuser_required(views.delete_wallet), name='delete_wallet'),
    path('customer/<int:user_id>/', superuser_required(views.view_customer), name='view_customer'),
    path('collector/<int:user_id>/', superuser_required(views.view_collector), name='view_collector'),
    path('delete-collector/<int:user_id>/', superuser_required(views.delete_collector), name='delete_collector'),
    path('collection/<int:request_id>/', superuser_required(views.get_completed_collection), name='view_collection'),
]


# Define Custom Function to Check If The User is a Superuser


urlpatterns = [
    
    path('', views.index, name='Index'),
    path('dashboard/', views.dashboard, name='Dash'),
    path('add-type/', views.addType, name='Add Type'),
    path('waste-type/', views.WasteType, name='Waste Type'),
    path('customers/', views.list_customers, name='Customers'),
    path('collectors/', views.list_collectors, name='Collectors'),
    path('add-waste-type/', views.create_waste, name='Add WasteType'),
    path('edit-waste-type/<int:pk>/', views.edit_waste, name='edit_waste'),
    path('wallet/<int:wallet_id>/', views.view_wallet, name='view_wallet'),
    path('wallets/', views.get_collector_wallets, name='Collector Wallets'), 
    path('requests/', views.get_customer_requests, name='Pending Requests'),
    path('delete-waste/<int:pk>/', views.delete_waste, name='delete_waste'),
    path('collections/', views.get_completed_collections, name='Collections'),
    path('delete-wallet/<int:pk>/',views.delete_wallet, name='delete_wallet'),
    path('customer/<int:user_id>/', views.view_customer, name='view_customer'),
    path('collector/<int:user_id>/', views.view_collector, name='view_collector'),
    path('delete-collector/<int:user_id>/', views.delete_collector, name='delete_collector'),
    path('collection/<int:request_id>/', views.get_completed_collection, name='view_collection'),
    
    ]