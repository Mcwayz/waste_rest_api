from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('manage-users', views.users, name='Users'),
    path('home', views.dashboard, name='Dashboard'),
    path('collections', views.collections, name='Collections'),
    path('subscriptions', views.subscriptions, name='Subscriptions'),
    path('subscription-details', views.sub_details, name='Subscription Details'),
    ]