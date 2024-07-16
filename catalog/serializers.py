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



class AllCategoryChildSerializer(serializers.ModelSerializer):
    sub_category=serializers.SerializerMethodField()
    brand=serializers.SerializerMethodField()

    def get_sub_category(self,obj):
        subcategory=SubCategory.objects.all()
        return SubCategorySerializer(subcategory,many=True).data
    def get_brand(self,obj):
        brand=Brand.objects.all()
        return BrandSerializer(brand,many=True).data
    class Meta:
        model=Category
        fields='__all__'