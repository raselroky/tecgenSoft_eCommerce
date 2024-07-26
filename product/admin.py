from django.contrib import admin
from product.models import ProductUnit,ProductVariant,ProductVariantAttribute,ProductVariantReview


admin.site.register(ProductUnit)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantAttribute)
admin.site.register(ProductVariantReview)
