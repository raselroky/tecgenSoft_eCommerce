from django.urls import path
from .views import (
    BannerListCreateAPIView,BannerRetrieveUpdateDestroyAPIView,BannerAllListAPIView,
    CountryListCreateAPIView,CountryRetrieveUpdateDestroyAPIView,CountryAllListAPIView
)


urlpatterns = [
    path('banner-create', BannerListCreateAPIView.as_view(),name='banner-list-create'),
    path('banner-retrieve-update-destroy/<int:id>', BannerRetrieveUpdateDestroyAPIView.as_view(),name='banner-get-update-destroy'),
    path('banner-list', BannerAllListAPIView.as_view(),name='banner-all-list'),

    path('country-create', CountryListCreateAPIView.as_view(),name='country-list-create'),
    path('country-retrieve-update-destroy/<int:id>', CountryRetrieveUpdateDestroyAPIView.as_view(),name='country-get-update-destroy'),
    path('country-list', CountryAllListAPIView.as_view(),name='country-all-list'),

]