from rest_framework import serializers
from product.models import ProductUnit,ProductVariant,ProductVariantAttribute,ProductVariantReview
from campaign.models import Campaign,CampaignMember,DealOfTheWeek
from campaign.serializers import CampaignSerializer,CampaignMemberSerializer,DealOfTheWeekSerializer
from helper.func_cal import get_overall_discount_calculated_values


class ProductUnitSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=ProductUnit
        fields='__all__'
        

class ProductVariantSeriaizer(serializers.ModelSerializer):
    campaign=serializers.SerializerMethodField()
    deals_of_the_week=serializers.SerializerMethodField()
    # online_discount=serializers.SerializerMethodField()
    updated_selling_price=serializers.SerializerMethodField()

    def get_campaign(self,obj):
        campaign_member=CampaignMember.objects.filter(id=obj.id)
        amount=0.0
        if campaign_member.exists():
            campaign_member_get=CampaignMember.objects.get(id=obj.id)
            if campaign_member_get.discount_type=='flat':
                amount=float(campaign_member_get.discount_value)
            elif campaign_member_get.discount_type=='percentage':
                amount=float(campaign_member_get.discount_value/100)
            return {
                "id":campaign_member_get.id,
                "campaign":campaign_member_get.campaign.name,
                "discount_type":campaign_member_get.discount_type,
                "discount_value":campaign_member_get.discount_value,
                "calculate_amount":amount,
                "product_price_with":get_overall_discount_calculated_values(obj.id,obj.selling_price),
                "start_date":campaign_member_get.start_date,
                "end_date":campaign_member_get.end_date,
                "created_by":{
                    'id':campaign_member_get.created_by.id,
                    'username':campaign_member_get.created_by.username,
                    'email':campaign_member_get.created_by.email
                    }

            }
        return None
    
    def get_deals_of_the_week(self,obj):
        #print(obj.id)
        deals=DealOfTheWeek.objects.filter(product_variant__id=obj.id)
        amount=0.0
        if deals.exists():
            deals_get=DealOfTheWeek.objects.get(product_variant__id=obj.id)
            if deals_get.discount_type=='flat':
                amount=float(deals_get.discount_value)
            elif deals_get.discount_type=='percentage':
                amount=obj.selling_price*float(deals_get.discount_value/100)
            return {
                "id":deals_get.id,
                "discount_type":deals_get.discount_type,
                "discount_value":deals_get.discount_value,
                "calculate_amount":amount,
                "product_price_with":get_overall_discount_calculated_values(obj.id,obj.selling_price),
                "start_date":deals_get.start_date,
                "end_date":deals_get.end_date,
                "created_by":{
                    'id':deals_get.created_by.id,
                    'username':deals_get.created_by.username,
                    'email':deals_get.created_by.email
                    }
            }
        return None
    
    def get_updated_selling_price(self,obj):
        if obj.discount_type=='flat':
            price=float(obj.selling_price-obj.online_discount)
        elif obj.discount_type=='percentage':
            price= float(obj.selling_price-float(obj.selling_price * (obj.online_discount/ 100) ))
        price=get_overall_discount_calculated_values(obj.id,obj.selling_price)
        if price<=0.0:
            price= obj.selling_price
        
        module=''
        campaign_member=CampaignMember.objects.filter(id=obj.id)
        deals=DealOfTheWeek.objects.filter(product_variant__id=obj.id)
        if campaign_member:
            module='campaign'
        elif deals:
            module='deals_of_the_week'
        elif obj.online_discount>0.0:
            module='online_discount'
        return {
            'updated_selling_price':price,
            "live":module
        }
    class Meta:
        model=ProductVariant
        fields='__all__'
        
        


class ProductvariantAttributeSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariantAttribute
        fields='__all__'


class ProductVariantReviewSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariantReview
        fields='__all__'


