from django import forms
from base.models import Waste

class WasteForm(forms.ModelForm):
    class Meta:
        model = Waste
        fields = ['waste_type', 'waste_desc', 'collection_price']