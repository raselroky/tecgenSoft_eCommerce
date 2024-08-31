from django.urls import path
from .views import (
    BannerListCreateAPIView,BannerRetrieveUpdateDestroyAPIView,BannerAllListAPIView,
    CountryListCreateAPIView,CountryRetrieveUpdateDestroyAPIView,CountryAllListAPIView,
    MultipleAddressListCreateAPIView,
    MultipleAddressRetreiveUpdateDestroyListAPIView,
    MultipleAddressAllListAPIView,ApplyCouponView
)


urlpatterns = [
    path('banner-create', BannerListCreateAPIView.as_view(),name='banner-list-create'),
    path('banner-retrieve-update-destroy/<int:id>', BannerRetrieveUpdateDestroyAPIView.as_view(),name='banner-get-update-destroy'),
    path('banner-list', BannerAllListAPIView.as_view(),name='banner-all-list'),

    path('country-create', CountryListCreateAPIView.as_view(),name='country-list-create'),
    path('country-retrieve-update-destroy/<int:id>', CountryRetrieveUpdateDestroyAPIView.as_view(),name='country-get-update-destroy'),
    path('country-list', CountryAllListAPIView.as_view(),name='country-all-list'),

    path('multipleaddress',MultipleAddressListCreateAPIView.as_view(),name='multiple-address-create'),
    path('multipleaddress/<int:id>',MultipleAddressRetreiveUpdateDestroyListAPIView.as_view(),name='multiple-address-retrieve-update-destroy'),
    path('multipleaddress-list',MultipleAddressAllListAPIView.as_view(),name='multiple-address-list'),

    path('apply-coupon/',ApplyCouponView.as_view(), name='apply-coupon'),

]