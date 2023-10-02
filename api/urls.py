from django.urls import path
from .views import collector_views, customer_views, admin_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


#URLs / Routes for endpoints

urlpatterns = [
    path('addWasteType/', admin_views.addWaste),
    path('wasteTypes/', customer_views.getWaste),
    path('customerRequests/', admin_views.getRequests),
    path('addCollection/', collector_views.addCollection),
    path('customers/', customer_views.getCustomerProfiles),
    path('collectors/', collector_views.getCollectorProfiles),
    path('updateCustomer/<str:pk>/', customer_views.updateUser),
    path('updateCollector/<str:pk>/', collector_views.updateUser),
    path('avaliableDrivers/', customer_views.viewAvailableDrivers),
    path('addCollectorProfile/', collector_views.addCollectorProfile),
    path('addCollector/', collector_views.create_user, name='create-user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('updateWaste/<str:pk>/', admin_views.updateWaste, name='update-waste'),
    path('wasteDetails/<str:pk>/', admin_views.wasteDetails, name='waste-details'),
    path('cancelRequest/<str:pk>/', customer_views.cancel_request, name='cancel-request'),
    path('customerDetails/<str:pk>/', customer_views.getCustomerProfile, name='user-details'),
    path('collectionDetails/<str:pk>/', customer_views.collectionDetails, name='collection-details'),
    path('collectorDetails/<str:pk>/', collector_views.getCollectorProfile, name='collector-details'),
]
