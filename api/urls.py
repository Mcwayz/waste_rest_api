from django.urls import path
from . import views

urlpatterns = [
    path('subscriptions', views.getSubscription),
    path('waste', views.getWaste),
    path('collections', views.getCollections),
    path('users', views.getUsers),
    path('addUser', views.addUser),
    path('addCollection', views.addCollection),
    path('addWasteType', views.addWaste),
    path('addSubscription', views.addSubscription),
]
