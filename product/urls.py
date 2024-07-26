from django.urls import path,include
from product.views import (
    ProductUnitListCreateAPIView,ProductUnitRetrieveUpdateDestroyAPIView,ProductVariantListCreateAPIView,ProductVariantRetrieveUpdateDestroyListCreateAPIView,
    ProductVariantAttributeListCreateAPIView,ProductVariantAttributeRetrieveUpdateDestroyAPIView,ProductVariantReviewListCreateAPIView,ProductVariantReviewRetrieveUpdateDestroyAPIView,
    PublicProductVariantAttributeListAPIView,PublicProductVariantAttributeRetrieveAPIView,PublicProductVariantListAPIView,PublicProductVariantRetrieveAPIView,
    PublicProductVariantReviewListAPIView,PublicProductVariantReviewretRieveAPIView
    )


urlpatterns=[
    #admin
    path('productunit-create/',ProductUnitListCreateAPIView.as_view(),name='product-unit-create-api'),
    path('productunit-retrieve-update-destroy/<int:id>',ProductUnitRetrieveUpdateDestroyAPIView.as_view(),name='product-unit-retrieve-update-destroy-api'),
    path('productvariant-create/',ProductVariantListCreateAPIView.as_view(),name='product-variant-create-api'),
    path('productvariant-retrieve-update-destroy/<int:id>',ProductVariantRetrieveUpdateDestroyListCreateAPIView.as_view(),name='product-variant-retrieve-update-destroy-api'),
    path('productvariant-attribute-create/',ProductVariantAttributeListCreateAPIView.as_view(),name='product-variant-attribute-create-api'),
    path('productvariant-attribute-retrieve-update-destroy/<int:id>',ProductVariantAttributeRetrieveUpdateDestroyAPIView.as_view(),name='product-variant-attribute-retrieve-update-destroy-api'),
    path('productvariant-review-create/',ProductVariantReviewListCreateAPIView.as_view(),name='product-variant-review-create-api'),
    path('productvariant-review-retrieve-update-destroy/<int:id>',ProductVariantReviewRetrieveUpdateDestroyAPIView.as_view(),name='product-variant-review-retrieve-update-destroy-api'),


    #users
    path('users-productvariant-list/',PublicProductVariantListAPIView.as_view(),name='user-product-variant-list'),
    path('users-productvariant-retrieve/<int:id>',PublicProductVariantRetrieveAPIView.as_view(),name='user-product-variant-retrieve'),
    path('users-productvariant-attribute-list/',PublicProductVariantAttributeListAPIView.as_view(),name='user-product-variant-attribute-list'),
    path('users-productvariant-attribute-retrieve/<int:id>',PublicProductVariantAttributeRetrieveAPIView.as_view(),name='user-product-variant-attribute-retrieve'),
    path('users-productvariant-review-list/',PublicProductVariantReviewListAPIView.as_view(),name='user-product-variant-review-list'),
    path('users-productvariant-review-retrieve/<int:id>',PublicProductVariantReviewretRieveAPIView.as_view(),name='user-product-variant-review-retrieve'),



]