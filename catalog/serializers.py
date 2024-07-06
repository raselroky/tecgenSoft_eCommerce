from rest_framework import serializers
from catalog.models import Category,SubCategory,Brand

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    
    class Meta:
        model=Category
        fields='__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    
    class Meta:
        model=SubCategory
        fields='__all__'

class BrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
   
    class Meta:
        model=Brand
        fields='__all__'