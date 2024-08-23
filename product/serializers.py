from rest_framework import serializers
from product.models import ProductUnit,ProductVariant,ProductVariantAttribute,ProductVariantReview

class ProductUnitSeriaizer(serializers.ModelSerializer):
    class Meta:
        model=ProductUnit
        fields='__all__'
        

class ProductVariantSeriaizer(serializers.ModelSerializer):
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
