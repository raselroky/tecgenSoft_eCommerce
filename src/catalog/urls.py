from django.urls import path,include
from catalog.views import (CategoryListCreateAPIView,CategoryRetrieveUpdateDestroyAPIView,SubCategoryListCreateAPIView,SubCategoryRetrieveUpdateDestroyAPIView,BrandListCreateAPIView,BrandRetrieveUpdateDestroyAPIView,PublicAllCategoryListAPIView,AttributeListCreateAPIView,AttributevalueListCreateAPIView,AttributeRetrieveUpdateDestroyAPIView,AttributevalueRetrieveUpdateDestroyAPIView,
                           UserBrandAllListAPIView,UserCateogryAllListAPIView,UserSubCateogryAllListAPIView
                )

            

urlpatterns=[
    path('category/',CategoryListCreateAPIView.as_view(),name='category-create-list-api'),
    path('category-retrieve-update-destroy/<int:id>',CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-retrieve-update-destroy'),
    path('subcategory/',SubCategoryListCreateAPIView.as_view(),name='subcategory-create-list-api'),
    path('subcategory-retrieve-update-destroy/<int:id>',SubCategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-retrieve-update-destroy'),
    path('brand/',BrandListCreateAPIView.as_view(),name='brand-create-list-api'),
    path('brand-retrieve-update-destroy/<int:id>',BrandRetrieveUpdateDestroyAPIView.as_view(),name='brand-retrieve-update-destroy'),

    path('user-all-categories/',PublicAllCategoryListAPIView.as_view(),name='all-list'),

    path('attribute-create/',AttributeListCreateAPIView.as_view(),name='attribute-create-api'),
    path('attribute-update-destroy/<int:id>',AttributeRetrieveUpdateDestroyAPIView.as_view(),name='attribute-retrieve-update-destroy-api'),
    path('attribute-value-create/',AttributevalueListCreateAPIView.as_view(),name='attribute-value-create-api'),
    path('attribute-value-update-destroy/<int:id>',AttributevalueRetrieveUpdateDestroyAPIView.as_view(),name='attribute-value-retrieve-update-destroy-api'),

    #user
    path('user-category/',UserCateogryAllListAPIView.as_view(),name='user-category-api'),
    path('user-subcategory/',UserSubCateogryAllListAPIView.as_view(),name='user-subcategory-api'),
    path('user-brand/',UserBrandAllListAPIView.as_view(),name='user-brand-api'),

]