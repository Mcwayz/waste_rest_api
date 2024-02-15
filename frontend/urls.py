from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Index'),
    path('map', views.map_view, name='map'),
    path('manage-users', views.users, name='Users'),
    path('add-user', views.add_user, name='Add User'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('collections', views.collections, name='Collections'),
    path('collection-requests', views.collection_requests, name='Requests'),
    path('collection-details/<int:pk>/', views.collection_details, name='collection_details'),
    path('collection-summary/<int:pk>/', views.collection_summary, name='collection_summary'),
    ]