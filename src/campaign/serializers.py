from rest_framework import serializers
from campaign.models import Campaign,CampaignMember,DealOfTheWeek


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignMember
        fields = '__all__'


class DealOfTheWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealOfTheWeek
        fields = '__all__'