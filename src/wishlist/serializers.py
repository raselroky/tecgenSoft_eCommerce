from rest_framework import serializers
from product.models import ProductVariant
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
from django.db.models import Prefetch,Avg,Sum,Q
from wishlist.models import Wishlist
from helper.func_cal import get_overall_discount_calculated_values



class WishlistSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'