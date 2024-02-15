from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Index'),
    path('map', views.map_view, name='map'),
    path('manage-users', views.users, name='Users'),
    path('dashboard', views.dashboard, name='Dash'),
    path('add-type', views.addType, name='Add Type'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('waste-type', views.WasteType, name='Waste Type'),
    path('collections', views.collections, name='Collections'),
    path('collection-requests', views.collection_requests, name='Requests'),
    path('collection-details/<int:pk>/', views.collection_details, name='collection_details'),
    path('collection-summary/<int:pk>/', views.collection_summary, name='collection_summary'),
    ]