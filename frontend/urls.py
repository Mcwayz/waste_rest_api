from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.dashboard, name='Index'),
    path('dashboard', views.dashboard, name='Dash'),
    path('add-type', views.addType, name='Add Type'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('waste-type', views.WasteType, name='Waste Type'),
    path('customers', views.list_customers, name='Customers'),
    path('collectors', views.list_collectors, name='Collectors'),
    path('add-waste-type', views.create_waste, name='Add WasteType'),
    path('wallet/<int:wallet_id>/', views.view_wallet, name='view_wallet'),
    path('wallets', views.get_collector_wallets, name='Collector Wallets'), 
    path('requests', views.get_customer_requests, name='Pending Requests'),
    path('edit-waste-type/<int:pk>/', views.edit_waste, name='edit_waste'),
    path('delete-waste/<int:pk>/', views.delete_waste, name='delete_waste'),
    path('collections', views.get_completed_collections, name='Collections'),
    path('delete-wallet/<int:pk>/',views.delete_wallet, name='delete_wallet'),
    path('customer/<int:user_id>/', views.view_customer, name='view_customer'),
    path('collector/<int:user_id>/', views.view_collector, name='view_collector'),
    path('delete-collector/<int:user_id>/', views.delete_collector, name='delete_collector'),
    path('collection/<int:request_id>/', views.get_completed_collection, name='view_collection'),
    
    ]