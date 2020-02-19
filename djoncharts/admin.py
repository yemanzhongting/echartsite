from django.contrib import admin

# Register your models here.
from djoncharts.models import AddressInfo,UserInfo
admin.site.register(UserInfo)
admin.site.register(AddressInfo)
