from rest_framework import serializers
from catalog.models import Category,SubCategory,Brand,AttributeValue,Attribute

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    
    class Meta:
        model=Category
        fields='__all__'



class BrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
   
    class Meta:
        model=Brand
        fields='__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    brand=serializers.SerializerMethodField()
    
    def get_brand(self,obj):
        brand=Brand.objects.filter(sub_category__name=obj)
        return BrandSerializer(brand,many=True).data

    class Meta:
        model=SubCategory
        fields='__all__'

class AllCategoryChildSerializer(serializers.ModelSerializer):
    sub_category=serializers.SerializerMethodField()
    # brand=serializers.SerializerMethodField()

    def get_sub_category(self,obj):
        subcategory=SubCategory.objects.filter(category__name=obj)
        return SubCategorySerializer(subcategory,many=True).data
    # def get_brand(self,obj):
    #     brand=Brand.objects.filter(category__name=obj)
    #     return BrandSerializer(brand,many=True).data
    class Meta:
        model=Category
        fields='__all__'


class AttributeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
   
    class Meta:
        model=Attribute
        fields='__all__'
class AttributeValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
   
    class Meta:
        model=AttributeValue
        fields='__all__'