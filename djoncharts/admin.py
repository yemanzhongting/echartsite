from django.contrib import admin

# Register your models here.
from djoncharts.models import AddressInfo,UserInfo,WeiboInfo,coronavirus,VirusInfo

admin.site.register(UserInfo)
admin.site.register(AddressInfo)
admin.site.register(WeiboInfo)
admin.site.register(coronavirus)
admin.site.register(VirusInfo)