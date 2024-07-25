from django.urls import path
from store.views import (
    VendorStoreCreateAPIView,
    VendorStoreRetrieveUpdateAPIView,
    VendorStoreGetAPIView,PublicStoreListAPIView
)


urlpatterns = [
    path('store-create', VendorStoreCreateAPIView.as_view(),
         name='vendor-store-list-create'),
    path('store-retrieve-update/<int:id>', VendorStoreRetrieveUpdateAPIView.as_view(),
         name='vendor-store-get-update'),
    path('get-store', VendorStoreGetAPIView.as_view(),
         name='vendor-store-get'),

    path('public-store-list',PublicStoreListAPIView.as_view(),name='public-store-list'),

]
