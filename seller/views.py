from django.shortcuts import render, redirect
from .forms import SellerRegistrationForm
from django.contrib.auth.models import User

def seller_success(request):
    return render(request, 'seller/success.html')

def seller_register(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['shop_name'],
                password="defaultpassword"
            )
            seller = form.save(commit=False)
            seller.user = user
            seller.save()
            return redirect('seller_success')
    else:
        form = SellerRegistrationForm()
    return render(request, 'seller/register.html',{'form':form})
