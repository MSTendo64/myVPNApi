from django.contrib import admin
from .models import VPNServer, APIKey

class VPNServerAdmin(admin.ModelAdmin):
       list_display = ('name',)

class APIKeyAdmin(admin.ModelAdmin):
       list_display = ('api_key',)

admin.site.register(VPNServer, VPNServerAdmin)
admin.site.register(APIKey, APIKeyAdmin)