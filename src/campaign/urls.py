from django.urls import path,include
from campaign.views import CampaignListCreateAPIView,CampaignRetrieveUpdateDestroyAPIView,CampaignMemberListCreateAPIView,CampaignMemberRetrieveUpdateDestroyAPIView,DealOfTheWeekListCreateAPIView,DealOfTheWeekRetrieveUpdateDestroyAPIView,PublicCampaignListAPIView,PublicCampaignMemberListAPIView,PublicDealOfTheWeekListAPIView

urlpatterns=[
    path('campaign-create/',CampaignListCreateAPIView.as_view(),name='campaign-create-api'),
    path('campaign-retrieve-update-delete/<int:id>',CampaignRetrieveUpdateDestroyAPIView.as_view(),name='campaign-retrieve-update-destroy-api'),
    path('campaign-member-create/',CampaignMemberListCreateAPIView.as_view(),name='campaign-member-create-api'),
    path('campaign-member-retrieve-update-delete/<int:id>',CampaignMemberRetrieveUpdateDestroyAPIView.as_view(),name='campaign-member-retrieve-update-destroy-api'),
    path('dealoftheweek-create/',DealOfTheWeekListCreateAPIView.as_view(),name='dealoftheweek-create-api'),
    path('dealoftheweek-retrieve-update-delete/<int:id>',DealOfTheWeekRetrieveUpdateDestroyAPIView.as_view(),name='dealoftheweek-retrieve-update-destroy-api'),


    path('users-campaign-list/',PublicCampaignListAPIView.as_view(),name='users-cmapign-list'),
    path('users-campaign-member-list/',PublicCampaignMemberListAPIView.as_view(),name='users-cmapign-member-list'),
    path('users-dealoftheweek-list/',PublicDealOfTheWeekListAPIView.as_view(),name='users-dealoftheweek-list'),


]