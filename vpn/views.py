from django.http import JsonResponse
from .models import VPNServer, APIKey
#import subprocess

def get_public_key():
    try:
        api_key = APIKey.objects.first()  # Получаем первый API-ключ
        return api_key.api_key if api_key else None
    except APIKey.DoesNotExist:
        return None

def verify_signature(pubKey, value):
    return pubKey == value

def get_all_vpn(request):
    value = request.headers.get('X-API-Key')

    if not value or value != get_public_key():
        return JsonResponse("api key Error", safe=False)

    servers = VPNServer.objects.all().values('id', 'name')
    return JsonResponse(list(servers), safe=False)

def get_vpn(request, vpn_number):
    value = request.headers.get('X-API-Key')

    if not value or value != get_public_key():
        return JsonResponse("api key Error", safe=False)
    
    try:
        server = VPNServer.objects.get(id=vpn_number)
        data = {
            'name': server.name,
            'countryCode': server.countryCode,
            'configuration': server.configuration
           }
        return JsonResponse(data)
    except VPNServer.DoesNotExist:
        return JsonResponse({'error': 'VPN not found'}, status=404)