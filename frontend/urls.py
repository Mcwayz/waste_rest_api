from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('map', views.map_view, name='map'),
    path('overdue', views.overdue, name='Overdue'),
    path('add-user', views.add_user, name='Add User'),
    path('manage-users', views.users, name='Users'),
    path('home', views.dashboard, name='Admin Dashboard'),
    path('collections', views.collections, name='Collections'),
    path('subscriptions', views.subscriptions, name='Subscriptions'),
    path('sub-details/<int:pk>/', views.sub_details, name='sub_details'),
    path('collection-requests', views.collection_requests, name='Requests'),
    path('collection-details/<int:pk>/', views.collection_details, name='collection_details'),
    path('collection-summary/<int:pk>/', views.collection_summary, name='collection_summary'),
    ]