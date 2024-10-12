from rest_framework import serializers
from catalog.models import Category,SubCategory,Brand,AttributeValue,Attribute

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_by=serializers.SerializerMethodField()
    updated_by=serializers.SerializerMethodField()
    def get_created_by(self,obj):
        if obj.created_by:
            return {
                "id":obj.created_by.id,
                "username":obj.created_by.username
            }
        return None
    def get_updated_by(self,obj):
        if obj.updated_by:
            return {
                "id":obj.updated_by.id,
                "username":obj.updated_by.username
            }
        return None
    class Meta:
        model=Category
        fields='__all__'



class BrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_by=serializers.SerializerMethodField()
    updated_by=serializers.SerializerMethodField()
    sub_category=serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), required=True)
    def get_created_by(self,obj):
        if obj.created_by:
            return {
                "id":obj.created_by.id,
                "username":obj.created_by.username
            }
        return None
    def get_updated_by(self,obj):
        if obj.updated_by:
            return {
                "id":obj.updated_by.id,
                "username":obj.updated_by.username
            }
        return None
    def get_sub_category(self,obj):
        if obj.sub_category:
            return {
                "id":obj.sub_category.id,
                "name":obj.sub_category.name
            }
        return None
    class Meta:
        model=Brand
        fields='__all__'
        


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    brand=serializers.SerializerMethodField()
    # category=serializers.SerializerMethodField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)

    created_by=serializers.SerializerMethodField()
    updated_by=serializers.SerializerMethodField()
    def get_created_by(self,obj):
        if obj.created_by:
            return {
                "id":obj.created_by.id,
                "username":obj.created_by.username
            }
        return None
    def get_updated_by(self,obj):
        if obj.updated_by:
            return {
                "id":obj.updated_by.id,
                "username":obj.updated_by.username
            }
        return None

    def get_brand(self,obj):
        brand=Brand.objects.filter(sub_category__name=obj)
        return BrandSerializer(brand,many=True).data

    # def get_category(self,obj):
    #     if obj.category:
    #         return {
    #             "id":obj.category.id,
    #             "name":obj.category.name
    #         }
    #     return None
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
    created_by=serializers.SerializerMethodField()
    updated_by=serializers.SerializerMethodField()
    def get_created_by(self,obj):
        if obj.created_by:
            return {
                "id":obj.created_by.id,
                "username":obj.created_by.username
            }
        return None
    def get_updated_by(self,obj):
        if obj.updated_by:
            return {
                "id":obj.created_by.id,
                "username":obj.updated_by.username
            }
        return None
    class Meta:
        model=Attribute
        fields='__all__'
class AttributeValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_by=serializers.SerializerMethodField()
    updated_by=serializers.SerializerMethodField()
    def get_created_by(self,obj):
        if obj.created_by:
            return {
                "id":obj.created_by.id,
                "username":obj.created_by.username
            }
        return None
    def get_updated_by(self,obj):
        if obj.updated_by:
            return {
                "id":obj.updated_by.id,
                "username":obj.updated_by.username
            }
        return None
    class Meta:
        model=AttributeValue
        fields='__all__'