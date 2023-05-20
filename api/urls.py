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
    path('waste-types', views.getWaste),
    path('add-wastetype', views.addWaste),
    path('add-profile', views.addProfile),
    path('collections', views.getCollected),
    path('add-collection', views.addCollection),
    path('subscriptions', views.getSubscription),
    path('add-subscription', views.addSubscription),
    path('collection-requests', views.getCollections),
    path('add-user/', views.create_user, name='create-user'),
    path('user-details/<str:pk>/', views.getUser, name='user-details'),
    path('update-user/<str:pk>/', views.updateUser, name='update-user'),
    path('profile-details/<int:auth_id>/', views.getUserDetails, name='user-details'),
    path('update-waste/<str:pk>/', views.updateWaste, name='update-waste'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('waste-details/<str:pk>/', views.wasteDetails, name='waste-details'),
    path('update-subscription/<str:pk>/', views.updateUser, name='update-subscription'),
    path('update-collection/<str:pk>/', views.update_collection, name='update-collection'),
    path('collection-details/<str:pk>/', views.collectionDetails, name='collection-details'),
    path('subscription-details/<str:pk>', views.subscriptionDetails, name='subscription-details'),
]
