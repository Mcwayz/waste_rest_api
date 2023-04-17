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
    path('collection-requests', views.collection_requests, name='Requests'),
    path('subscription-details', views.sub_details, name='Subscription Details'),
    ]