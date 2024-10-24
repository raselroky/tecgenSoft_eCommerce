from django.urls import path,include
from product.views import (
    ProductUnitListCreateAPIView,ProductUnitRetrieveUpdateDestroyAPIView,ProductVariantListCreateAPIView,ProductVariantRetrieveUpdateDestroyAPIView,
    ProductVariantAttributeListCreateAPIView,ProductVariantAttributeRetrieveUpdateDestroyAPIView,ProductVariantReviewListCreateAPIView,ProductVariantReviewRetrieveUpdateDestroyAPIView,
    PublicProductVariantAttributeListAPIView,PublicProductVariantAttributeRetrieveAPIView,PublicProductVariantListAPIView,PublicProductVariantRetrieveAPIView,
    PublicProductVariantReviewListAPIView,PublicProductVariantReviewretRieveAPIView,PublicNewArrivalProductVariantListAPIView,PublicRecentNewlyProductVariantListAPIView,


    )


urlpatterns=[
    #admin
    path('admin-productunit-create/',ProductUnitListCreateAPIView.as_view(),name='product-unit-create-api'),
    path('admin-productunit-retrieve-update-destroy/<int:id>',ProductUnitRetrieveUpdateDestroyAPIView.as_view(),name='product-unit-retrieve-update-destroy-api'),
    path('admin-productvariant-create/',ProductVariantListCreateAPIView.as_view(),name='product-variant-create-api'),
    path('admin-productvariant-retrieve-update-destroy/<int:id>',ProductVariantRetrieveUpdateDestroyAPIView.as_view(),name='product-variant-retrieve-update-destroy-api'),
    path('admin-productvariant-attribute-create/',ProductVariantAttributeListCreateAPIView.as_view(),name='product-variant-attribute-create-api'),
    path('admin-productvariant-attribute-retrieve-update-destroy/<int:id>',ProductVariantAttributeRetrieveUpdateDestroyAPIView.as_view(),name='product-variant-attribute-retrieve-update-destroy-api'),
    path('admin-productvariant-review-create/',ProductVariantReviewListCreateAPIView.as_view(),name='product-variant-review-create-api'),
    path('admin-productvariant-review-retrieve-update-destroy/<int:id>',ProductVariantReviewRetrieveUpdateDestroyAPIView.as_view(),name='product-variant-review-retrieve-update-destroy-api'),


    #users
    path('users-productvariant-list/',PublicProductVariantListAPIView.as_view(),name='user-product-variant-list'),
    path('users-productvariant-retrieve/<int:id>',PublicProductVariantRetrieveAPIView.as_view(),name='user-product-variant-retrieve'),
    path('users-productvariant-attribute-list/',PublicProductVariantAttributeListAPIView.as_view(),name='user-product-variant-attribute-list'),
    path('users-productvariant-attribute-retrieve/<int:id>',PublicProductVariantAttributeRetrieveAPIView.as_view(),name='user-product-variant-attribute-retrieve'),
    path('users-productvariant-review-list/',PublicProductVariantReviewListAPIView.as_view(),name='user-product-variant-review-list'),
    path('users-productvariant-review-retrieve/<int:id>',PublicProductVariantReviewretRieveAPIView.as_view(),name='user-product-variant-review-retrieve'),


    # path('best-selling-products',PublicBestSellingProductVariantListAPIView.as_view(),name='best-selling-products-list-api'),
    path('users-new-arrivals-products',PublicNewArrivalProductVariantListAPIView.as_view(),name='new-arrivals-products-list-api'),
    path('uers-recent-newly-products',PublicRecentNewlyProductVariantListAPIView.as_view(),name='newly-recent-products-list-api'),

    # path('users-cart-create/',UserCartItemListCreateAPIView.as_view(),name='user-cart-create-api'),
    # path('users-cart-retrieve-update-destroy/<int:id>',UserCartItemListRetrieveUpdateDestroyAPIView.as_view(),name='user-cart-retrieve-update-destroy-api'),




]