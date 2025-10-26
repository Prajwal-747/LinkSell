from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def clean_phone_number(phone):
    phone = phone.strip().replace(" ", "")
    if phone.startswith("+91") and len(phone)==13:
        return phone
    elif len(phone)==10 and phone.isdigit():
        return "+91"+phone
    else:
        raise ValidationError("Invalid Indian Phone Number format")

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.whatsapp_number = clean_phone_number(self.whatsapp_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.shop_name
