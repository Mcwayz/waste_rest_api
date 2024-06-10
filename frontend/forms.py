from django import forms
from base.models import Waste, ServiceCharge


# Waste Type Form


class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        fields = ['waste_type', 'waste_desc', 'collection_price']
   
#  Charge / Commission Form 
        
class ChargeForm(forms.ModelForm):
    class Meta:
        model = ServiceCharge
        fields = ['service_type', 'service_charge']