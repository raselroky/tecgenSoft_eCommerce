from django.contrib import admin
from user.models import User,UserAddress


class UsersAdminColumn(admin.ModelAdmin):
    list_display=['id','username','email','contact_number','date_joined','first_name','last_name','is_active','profile_pic','address','gender','last_login']
admin.site.register(User,UsersAdminColumn)

class UserAddressAdminColumn(admin.ModelAdmin):
    list_display=['id','user','address','created_at']
admin.site.register(UserAddress,UserAddressAdminColumn)