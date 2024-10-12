from django.contrib import admin
from campaign.models import Campaign,CampaignMember,DealOfTheWeek


class CampaignAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(Campaign,CampaignAdminColumn)

class CampaignMemberAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(CampaignMember,CampaignMemberAdminColumn)

class DealOfTheWeekAdminColumn(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]
    
    # Make all fields clickable
    def get_list_display_links(self, request, list_display):
        return list_display 
admin.site.register(DealOfTheWeek,DealOfTheWeekAdminColumn)
