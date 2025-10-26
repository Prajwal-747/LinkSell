from django.contrib import admin
from .models import Seller

# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display=('shop_name','user','verified','created_at')
    search_fields=('shop_name','user__username','whatsapp_number')
