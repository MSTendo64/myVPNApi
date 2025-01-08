from django.urls import path
from .views import get_all_vpn, get_vpn

urlpatterns = [
    path('api/get-all/', get_all_vpn, name='get_all_vpn'),
    path('api/get-vpn-<int:vpn_number>/', get_vpn, name='get_vpn'),
]
