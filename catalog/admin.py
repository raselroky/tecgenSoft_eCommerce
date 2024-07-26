from django.contrib import admin
from catalog.models import Category,SubCategory,Brand,Attribute,AttributeValue


class CategoryAdminColumn(admin.ModelAdmin):
    list_display=['id','created_by','updated_by','created_at','updated_at','name','show_in_ecommerce','ordering','icon','logo','is_active']
admin.site.register(Category,CategoryAdminColumn)

class SubCategoryAdminColumn(admin.ModelAdmin):
    list_display=['id','created_by','updated_by','created_at','updated_at','name','category','show_in_ecommerce','ordering','icon','logo','is_active']
admin.site.register(SubCategory,SubCategoryAdminColumn)

class BrandAdminColumn(admin.ModelAdmin):
    list_display=['id','created_by','updated_by','created_at','updated_at','name','category','sub_category','show_in_ecommerce','ordering','icon','logo','is_active']
admin.site.register(Brand,BrandAdminColumn)



admin.site.register(Attribute)
admin.site.register(AttributeValue)