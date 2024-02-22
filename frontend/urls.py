from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Index'),
    path('manage-users', views.users, name='Users'),
    path('dashboard', views.dashboard, name='Dash'),
    path('add-type', views.addType, name='Add Type'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('waste-type', views.WasteType, name='Waste Type'),
    path('add-waste-type', views.create_waste, name='Add WasteType'),
    path('edit-waste-type/<int:pk>/', views.edit_waste, name='edit_waste'),
    path('delete-waste/<int:pk>/', views.delete_waste, name='delete_waste'),
    path('collections', views.get_completed_collections, name='view_collection'),
    # path('collection/<int:pk>/', views.get_completed_collections, name='Collections'),
    ]