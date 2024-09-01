from django.urls import path
from store.views import (
    VendorStoreCreateAPIView,
    VendorStoreRetrieveUpdateDestroyAPIView,
    VendorStoreListAPIView,PublicStoreListAPIView,PublicStoreRetrieveAPIView
)


urlpatterns = [
    path('store-create', VendorStoreCreateAPIView.as_view(),
         name='vendor-store-list-create'),
    path('store-retrieve-update/<int:id>', VendorStoreRetrieveUpdateDestroyAPIView.as_view(),name='vendor-store-get-update'),
    path('store-list', VendorStoreListAPIView.as_view(),name='vendor-store-list'),

    path('users-store-list',PublicStoreListAPIView.as_view(),name='public-store-list'),
    path('users-store-retrieve/<int:id>',PublicStoreRetrieveAPIView.as_view(),name='public-store-retrieve'),

]
