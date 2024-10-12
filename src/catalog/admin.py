from django.contrib import admin
from catalog.models import Category,SubCategory,Brand,Attribute,AttributeValue


class CategoryAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(Category,CategoryAdminColumn)

class SubCategoryAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(SubCategory,SubCategoryAdminColumn)

class BrandAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(Brand,BrandAdminColumn)


class AttributeAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(Attribute,AttributeAdminColumn)

class AttributeValueAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(AttributeValue,AttributeValueAdminColumn)