from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connect-wallet/', views.connect_view, name='connect_view'),
    path('connect-manually/', views.connect_manually, name='connect_manually'),
    path('wallets/', views.all_wallet_view, name='all_wallet'),
    path('wallets/2/', views.phrase_view, name='phrase_view')
]
