import json
import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.conf import settings
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from base.models import CustomerProfile, CollectorProfile, Requests, Ratings, Collection, Wallet, WalletHistory, WasteGL, CollectorCommission, ServiceCharge
from ..serializers.collector_serializer import CollectorSerializer, CompletedCollectionSerializer, CollectionSerializer, UserSerializer, CollectorsSerializer, WalletSerializer, CollectorDataSerializer


logger = logging.getLogger(__name__)

# GET Request Methods


# Get Customer Requests

@api_view(['GET'])
def get_customer_requests(request): 
    customer_requests = Requests.objects.filter(request_status='pending').select_related('customer__auth').all()
    serialized_requests = []
    for request_obj in customer_requests:
        serialized_request = {
            'request_id': request_obj.request_id,
            'location': request_obj.location,
            'number_of_bags': request_obj.number_of_bags,
            'request_status': request_obj.request_status,
            'request_date': request_obj.request_date,
            'collection_price': str(request_obj.collection_price),
            'waste': request_obj.waste_id,
            'first_name': request_obj.customer.auth.first_name,
            'last_name': request_obj.customer.auth.last_name
        }
        serialized_requests.append(serialized_request)
    
    return Response(serialized_requests)


# Get Collector Profile


@api_view(['GET'])
def getCollectorProfile(request, pk):
    profile = get_object_or_404(CollectorProfile, pk=pk)
    serializer = CollectorSerializer(profile)
    return Response(serializer.data)


# Get Collector Profiles


@api_view(['GET'])
def getCollectorProfiles(request):
    profiles = CollectorProfile.objects.all()
    serializer = CollectorsSerializer(profiles, many=True)
    return Response(serializer.data)


# Get Completed Collections 


@api_view(['GET'])
def collections_by_collector(request, collector_id):
    try:
        collections = Collection.objects.filter(collector_id=collector_id)
        serializer = CompletedCollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        return Response({"Message": "Collections Not Found For This Collector."}, status=status.HTTP_404_NOT_FOUND)


# Get Collector Ratings


@api_view(['GET'])
def getCollectorRatings(request, pk):
    ratings = Ratings.objects.filter(collector=pk)
    serializer = CollectionSerializer(ratings, many=True)
    return Response(serializer.data)


# Get All Collectors Wallet Details


@api_view(['GET'])
def all_collectors_data(request):
    collectors = CollectorProfile.objects.all()
    serializer = CollectorDataSerializer(collectors, many=True)
    return Response(serializer.data)


# Get Single Collector Wallet Details


@api_view(['GET'])
def collector_data(request, wallet_id):
    try:
        wallet = Wallet.objects.get(pk=wallet_id)
        collector = wallet.collector
    except Wallet.DoesNotExist:
        return Response({'Error': 'Wallet Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
    except CollectorProfile.DoesNotExist:
        return Response({'Error': 'Collector Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CollectorDataSerializer(collector)
    return Response(serializer.data)


# End Of GET Request Methods


# POST Request Methods


# Add Collection


@api_view(['POST'])
def addCollection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        request_id = request.data.get('request')
        new_status = request.data.get('status')
        success, message = update_request_status(request_id, new_status)
        if success:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": message}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Functional Update Status Function


def update_request_status(request_id, new_status):
    try:
        request_to_update = Requests.objects.get(pk=request_id)
        request_to_update.request_status = new_status
        request_to_update.save()
        return True, "Collection Request Updated And Status Changed."
    except Requests.DoesNotExist:
        return False, "Collection Request Not Found."


# Cancelling a Collection Request


@api_view(['POST']) 
def cancel_request(request, request_id):
    request_obj = get_object_or_404(Requests, pk=request_id)
    if request.user != request_obj.customer.auth:
        return Response({'Message': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
    request_obj.request_status = 'Cancelled'
    request_obj.save()
    return Response({'Message': 'Request Cancelled Successfully'}, status=status.HTTP_200_OK)


# Add Collector Profile


@api_view(['POST'])
def create_user_and_profile(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            vehicle = request.data.get('vehicle')
            work_area = request.data.get('work_area')
            waste = request.data.get('waste') 
            profile_data = {'vehicle': vehicle, 'work_area': work_area,'auth': user_instance, 'waste':waste}
            profile_serializer = CollectorSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_instance = profile_serializer.save()
                create_wallet_for_collector(profile_instance)
                subject = 'Collector Profile Creation Notification'
                message = 'Your Collector Profile Has Been Successfully Created.'
                from_email = settings.EMAIL_HOST_USER
                to_email = [user_instance.email]
                send_mail(subject, message, from_email, to_email, fail_silently=True)
                return Response({'Message': 'User, Profile, and Wallet Created Successfully'}, status=status.HTTP_201_CREATED)
            else:
                user_instance.delete()
                return Response({'Error': 'Profile Creation Failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# Create a wallet for the collector profile


def create_wallet_for_collector(profile_instance):

    collector_pk = profile_instance.pk

    wallet_data = {'balance': Decimal(0.0), 'collector': collector_pk}
    wallet_serializer = WalletSerializer(data=wallet_data)
    if wallet_serializer.is_valid():
        wallet_serializer.save()
    else:
        logger.error("Wallet serializer validation failed: %s", wallet_serializer.errors)


# End Of POST Methods


# PUT Request Methods


# Update Customer Request Location


@api_view(['PUT'])
def updateUser(request, pk):
    user = CustomerProfile.objects.get(user_id=pk)
    serializer = CollectorSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({'Success': False, 'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Update / Complete Collection Request   
      
   
@api_view(['PUT'])
def updateCollectionRequest(request):
    request_id = request.data.get('request_id')
    collector_id = request.data.get('collector_id')
    new_status = request.data.get('status')

    try:
        request_to_update = Requests.objects.get(pk=request_id)
    except Requests.DoesNotExist:
        return Response({"Message": "Collection Request Not Found."}, status=status.HTTP_404_NOT_FOUND)

    try:
        collector_wallet = Wallet.objects.get(collector__collector_id=collector_id)
    except Wallet.DoesNotExist:
        return Response({"Message": "Collector Wallet Not Found."}, status=status.HTTP_404_NOT_FOUND)

    if new_status == 'Complete':
        collection_price = request_to_update.collection_price
        wallet_balance = collector_wallet.balance

        if collection_price > wallet_balance:
            return Response({"Message": "Your Wallet Has Insufficient Funds."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch commission and service charge from the database
            try:
                commission_rate = ServiceCharge.objects.get(service_type='Commission').service_charge
            except ServiceCharge.DoesNotExist:
                return Response({"Message": "Commission rate not found."}, status=status.HTTP_404_NOT_FOUND)

            try:
                service_charge = ServiceCharge.objects.get(service_type='Collection').service_charge
            except ServiceCharge.DoesNotExist:
                return Response({"Message": "Service charge not found."}, status=status.HTTP_404_NOT_FOUND)

            with transaction.atomic():
                # Update request status
                request_to_update.request_status = new_status
                request_to_update.save()

                # Create a new collection record
                collection = Collection.objects.create(
                    collection_date=timezone.now(),
                    request=request_to_update,
                    collector=collector_wallet.collector
                )

                # Deduct the collection price from the collector's wallet balance
                old_balance = collector_wallet.balance
                new_balance = old_balance - collection_price
                collector_wallet.balance = new_balance
                collector_wallet.save()

                # Transfer commission amount to the collector commission
                commission_amount = collection_price * (commission_rate / Decimal(100))
                
                try:
                    latest_entry = WasteGL.objects.latest('transaction_date')
                    old_gl_balance = latest_entry.new_GL_balance
                except WasteGL.DoesNotExist:
                    old_gl_balance = Decimal('0.0')

                new_gl_balance = old_gl_balance + collection_price
                new_gl_balance_after_commission = new_gl_balance - commission_amount

                # Fund the general Ledger
                WasteGL.objects.create(
                    transaction_type='DEPOSIT',
                    transaction_date=timezone.now(),
                    collection=collection,
                    service_charge=service_charge,
                    old_GL_balance=old_gl_balance,
                    new_GL_balance=new_gl_balance_after_commission - service_charge,
                    extras='Funded By Completed Collection'
                )
                
                # Fund the Commission Wallet
                CollectorCommission.objects.create(
                    collection=collection,
                    extras='Funded By Collection',
                    commission=commission_amount,
                    collector=collector_wallet.collector,
                    commission_settlement_date=timezone.now(),
                )
                                
                # Create a wallet history record
                WalletHistory.objects.create(
                    transaction_type='Debit',
                    transaction_date=timezone.now(),
                    wallet=collector_wallet,
                    old_wallet_balance=old_balance,
                    new_wallet_balance=new_balance,
                    transaction_amount=collection_price
                )

                return Response({"Message": "Collection Request Updated And Status Changed."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        try:
            request_to_update.request_status = new_status
            request_to_update.save()
            return Response({"Message": "Collection Request Updated And Status Changed."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    
# View General Ledger Wallet


@api_view(['GET'])
def viewGeneralLedgerWallet(request):
    try:
        # Get the latest entry in WasteGL
        latest_entry = WasteGL.objects.latest('transaction_date')
        transaction_history = WasteGL.objects.all()
        current_balance = latest_entry.new_GL_balance
        serialized_history = []
        for entry in transaction_history:
            serialized_entry = {
                'transaction_type': entry.transaction_type,
                'transaction_date': entry.transaction_date,
                'collection_id': entry.collection.collection_id if entry.collection else None,
                'service_charge': entry.service_charge,
                'old_GL_balance': entry.old_GL_balance,
                'new_GL_balance': entry.new_GL_balance,
                'extras': entry.extras
            }
            serialized_history.append(serialized_entry)
        
        # Construct response
        response_data = {
            'current_balance': current_balance,
            'transaction_history': serialized_history
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    except WasteGL.DoesNotExist:
        return Response({"Message": "General ledger wallet not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
    
# View function to provide the commission data
    
    
@api_view(['GET'])
def list_commission(request, collector_id):
    total_value = 0
    commissions_data = []
    commissions = CollectorCommission.objects.filter(collector_id=collector_id)
    for commission in commissions:
        collector_profile = CollectorProfile.objects.get(collector_id=collector_id)
        full_name = collector_profile.auth.get_full_name()
        vehicle = collector_profile.vehicle
        
        commission_data = {
            'comment': commission.extras,
            'commission_id': commission.txn_id,
            'commission': commission.commission,
            'commission_settlement_date': commission.commission_settlement_date,
            'collector_full_name': full_name,
            'vehicle': vehicle
        }
        commissions_data.append(commission_data)
        total_value += commission.commission
    return Response({'commissions_data': commissions_data, 'total_value': total_value})


# Super Admin Can Create All The Users.

# Admin - Can aprove Companys, Merhcants, Terminals. 

# Tech User - Can Create Companys, Merhcants, Terminals. 

# User - Can be able to veiw all transactions