from django.contrib import admin
from cartitem.models import CartItem

class CartItemAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(CartItem,CartItemAdminColumn)