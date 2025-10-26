from django import forms
from .models import Seller

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['shop_name','whatsapp_number','email','address']