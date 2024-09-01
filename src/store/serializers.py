from rest_framework import serializers
from store.models import Store, StorePaymentMethod
from user.serializers import UserSerializer,UserLiteSerializer
from django.db.models import Sum, Q, Avg


class StoreSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()
    
    def get_latitude(self, obj):
        return obj.latitude()

    def get_longitude(self, obj):
        return obj.longitude()

    def get_users(self, obj):
        if obj.user_set.all().exists():
            return UserLiteSerializer(obj.user_set.all(), many=True).data
        else:
            return None

    
    class Meta:
        model = Store
        fields = [
            'id', 
            'name',
            'email',
            'address', 
            'primary_phone',
            'latitude',
            'longitude', 
            'is_active',
            'created_at', 
            'updated_at', 
            'created_by', 
            'updated_by', 
            'off_days', 
            'shown_in_website', 
            'closing_time',
            'opening_time', 
            'map_link',
            'users', 
            'logo',
            'cover_photo', 
            'bio', 
            'about',
            'policies'
        ]
    
    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        store.is_active=False
        
        store.save()
        return store

   

class StoreLiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = '__all__'


class StorePaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model=StorePaymentMethod
        fields='__all__'