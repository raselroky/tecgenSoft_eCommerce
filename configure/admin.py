from django.contrib import admin
from .models import Country,Banner,PlatformCoupon,AllUsedCoupon,MultipleAddress

admin.site.register(Country)
admin.site.register(Banner)
admin.site.register(PlatformCoupon)
admin.site.register(AllUsedCoupon)
admin.site.register(MultipleAddress)