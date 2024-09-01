from rest_framework import serializers
from .models import Banner,Country,MultipleAddress,PlatformCoupon,AllUsedCoupon

class BannerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model=Banner
        fields='__all__'
    

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     user = request.user if request else None
    #     if user and user.is_authenticated:
    #         user = user._wrapped if hasattr(user, '_wrapped') else user
    #     validated_data['created_by'] = user
    #     return super(BannerSerializer, self).create(validated_data)
        
class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model=Country
        fields='__all__'

class MultipleAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=MultipleAddress
        fields= "__all__"

class PlatformCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlatformCoupon
        fields= "__all__"
class AllUsedCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllUsedCoupon
        fields= "__all__"