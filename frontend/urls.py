from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Index'),
    path('dashboard', views.dashboard, name='Dash'),
    path('add-type', views.addType, name='Add Type'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('waste-type', views.WasteType, name='Waste Type'),
    path('add-waste-type', views.create_waste, name='Add WasteType'),
    path('requests', views.get_customer_requests, name='Pending Requests'),
    path('edit-waste-type/<int:pk>/', views.edit_waste, name='edit_waste'),
    path('delete-waste/<int:pk>/', views.delete_waste, name='delete_waste'),
    path('collections', views.get_completed_collections, name='Collections'),
    path('collection/<int:request_id>/', views.get_completed_collection, name='view_collection'),
    ]