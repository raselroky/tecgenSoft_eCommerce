from django.urls import path
from .views import (
    BannerListCreateAPIView,BannerRetrieveUpdateDestroyAPIView,BannerAllListAPIView,
    CountryListCreateAPIView,CountryRetrieveUpdateDestroyAPIView,CountryAllListAPIView,
    MultipleAddressListCreateAPIView,
    MultipleAddressRetreiveUpdateDestroyListAPIView,
    MultipleAddressAllListAPIView,ApplyCouponView
)


urlpatterns = [
    path('admin-banner-create', BannerListCreateAPIView.as_view(),name='banner-list-create'),
    path('admin-banner-retrieve-update-destroy/<int:id>', BannerRetrieveUpdateDestroyAPIView.as_view(),name='banner-get-update-destroy'),
    path('admin-banner-list', BannerAllListAPIView.as_view(),name='banner-all-list'),
    path('users-banner-list', BannerAllListAPIView.as_view(),name='banner-all-list'),

    path('admin-country-create', CountryListCreateAPIView.as_view(),name='country-list-create'),
    path('admin-country-retrieve-update-destroy/<int:id>', CountryRetrieveUpdateDestroyAPIView.as_view(),name='country-get-update-destroy'),
    path('admin-country-list', CountryAllListAPIView.as_view(),name='country-all-list'),
    path('users-country-list', CountryAllListAPIView.as_view(),name='country-all-list'),

    path('users-multipleaddress',MultipleAddressListCreateAPIView.as_view(),name='multiple-address-create'),
    path('users-multipleaddress/<int:id>',MultipleAddressRetreiveUpdateDestroyListAPIView.as_view(),name='multiple-address-retrieve-update-destroy'),
    path('users-multipleaddress-list',MultipleAddressAllListAPIView.as_view(),name='multiple-address-list'),

    path('apply-coupon/',ApplyCouponView.as_view(), name='apply-coupon'),

]