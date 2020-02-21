from django.contrib import admin

# Register your models here.
from djoncharts.models import AddressInfo,UserInfo,WeiboInfo,coronavirus

admin.site.register(UserInfo)
admin.site.register(AddressInfo)
admin.site.register(WeiboInfo)
admin.site.register(coronavirus)