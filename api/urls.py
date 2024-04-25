from django.urls import path
from .views import collector_views, customer_views, admin_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    
    path('addUser/', admin_views.create_user),
    path('addWasteType/', admin_views.addWaste),
    path('wasteTypes/', customer_views.getWaste),    
    path('addCollection/', collector_views.addCollection),
    path('customers/', customer_views.getCustomerProfiles),
    path('collectors/', collector_views.getCollectorProfiles),
    path('updateCustomer/<str:pk>/', customer_views.updateUser),
    path('addCollectionRequest/', customer_views.create_request),
    path('updateCollector/<str:pk>/', collector_views.updateUser),
    path('updateRequest/', collector_views.updateCollectionRequest),
    path('customerRequests/', collector_views.get_customer_requests),
    path('addCustomerProfile/', customer_views.create_user_and_profile),
    path('completeCollection/', collector_views.updateCollectionRequest),
    path('completedCollections/', admin_views.get_completed_collections),
    path('addCollectorProfile/', collector_views.create_user_and_profile),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('updateWaste/<str:pk>/', admin_views.updateWaste, name='update-waste'),
    path('wasteDetails/<str:pk>/', admin_views.wasteDetails, name='waste-details'),
    path('wallets/', collector_views.all_collectors_data, name='all-collectors-data'),
    path('cancelRequest/<str:pk>/', customer_views.cancel_request, name='cancel-request'),
    path('collectorCollections/<int:collector_id>/', collector_views.collections_by_collector),
    path('collector/<int:collector_id>/', collector_views.collector_data, name='collector-data'),
    path('view-wallet/<int:wallet_id>/', collector_views.collector_data, name='collectors-data'),
    path('customerDetails/<str:pk>/', customer_views.getCustomerProfile, name='customer-details'),
    path('customerCollections/<int:customer_id>/', customer_views.completed_collections_by_customer),
    path('collectionDetails/<str:pk>/', customer_views.collectionDetails, name='collection-details'),
    path('collectorDetails/<str:pk>/', collector_views.getCollectorProfile, name='collector-details'),
    path('total_collections_per_month/', admin_views.total_collections_per_month, name='total_collections_per_month'),
    path('completedCollection/<int:request_id>/', admin_views.get_completed_collection, name='get_completed_collection'),
    
]
