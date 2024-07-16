from django.urls import path,include
from catalog.views import CategoryListCreateAPIView,CategoryRetrieveUpdateDestroyAPIView,SubCategoryListCreateAPIView,SubCategoryRetrieveUpdateDestroyAPIView,BrandListCreateAPIView,BrandRetrieveUpdateDestroyAPIView,PublicAllCategoryListAPIView
            

urlpatterns=[
    path('category/',CategoryListCreateAPIView.as_view(),name='category-create-list-api'),
    path('category-retrieve-update-destroy/<int:id>',CategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-retrieve-update-destroy'),
    path('subcategory/',SubCategoryListCreateAPIView.as_view(),name='subcategory-create-list-api'),
    path('subcategory-retrieve-update-destroy/<int:id>',SubCategoryRetrieveUpdateDestroyAPIView.as_view(),name='category-retrieve-update-destroy'),
    path('brand/',BrandListCreateAPIView.as_view(),name='brand-create-list-api'),
    path('brand-retrieve-update-destroy/<int:id>',BrandRetrieveUpdateDestroyAPIView.as_view(),name='brand-retrieve-update-destroy'),

     path('all-categories/',PublicAllCategoryListAPIView.as_view(),name='all-list'),



]