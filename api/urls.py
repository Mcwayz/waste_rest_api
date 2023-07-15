from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


#URLs / Routes for endpoints

urlpatterns = [
    path('', views.apiOverview),
    path('users', views.getUsers),
    path('tasks', views.getTasks),
    path('waste-types', views.getWaste),
    path('add-wastetype', views.addWaste),
    path('add-profile', views.addProfile),
    path('collectors', views.getCollectors),
    path('collections', views.getCollected),
    path('add-collector', views.addCollector),
    path('assign-collector', views.addAssignment),
    path('add-collection', views.addCollection),
    path('subscriptions', views.getSubscription),
    path('add-subscription', views.addSubscription),
    path('my-tasks/<int:auth_id>/', views.getMyTasks),
    path('collection-requests', views.getCollections),
    path('my-subscriptions/<int:auth_id>/', views.mySubs),
    path('add-user/', views.create_user, name='create-user'),
    path('collector/<str:pk>/', views.getCollector, name='Collector'),
    path('user-details/<str:pk>/', views.getUser, name='user-details'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('update-waste/<str:pk>/', views.updateWaste, name='update-waste'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('waste-details/<str:pk>/', views.wasteDetails, name='waste-details'),
    path('profile-details/<int:auth_id>/', views.getUserDetails, name='user-details'),
    path('update-subscription/<str:pk>/', views.updateUser, name='update-subscription'),
    path('update-collection/<str:pk>/', views.update_collection, name='update-collection'),
    path('collection-details/<str:pk>/', views.collectionDetails, name='collection-details'),
    path('collector-details/<int:auth_id>/', views.getCollectorDetails, name='collector-details'),
    path('subscription-details/<str:pk>', views.subscriptionDetails, name='subscription-details'),
]
