from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview),
    path('subscriptions', views.getSubscription),
    path('waste-types', views.getWaste),
    path('collections', views.getCollections),
    path('users', views.getUsers),
    path('add-user', views.addUser),
    path('add-collection', views.addCollection),
    path('add-wastetype', views.addWaste),
    path('add-subscription', views.addSubscription),
    path('subscription-details/<str:pk>', views.subscriptionDetails, name='subscription-details'),
    path('waste-details/<str:pk>/', views.wasteDetails, name='waste-details'),
    path('collection-details/<str:pk>/', views.collectionDetails, name='collection-details'),
    path('user-details/<str:pk>/', views.getUser, name='user-details'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('update-collection/<str:pk>/', views.updateCollection, name='update-collection'),
    path('update-waste/<str:pk>/', views.updateWaste, name='update-waste'),
    path('update-subscription/<str:pk>/', views.updateUser, name='update-subscription'),
]
