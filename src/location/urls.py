from django.urls import path
from .views import (
    AdminDivisionListCreateAPIView,AdminDivisionListAPIView,AdminDivisionRetrieveUpdateDestroyAPIView,
    AdminDistrictListCreateAPIView,AdminDistrictListAPIView,AdminDistrictRetrieveUpdateDestroyAPIView,
    UsersDivisionListAPIView,UsersDistrictListAPIView
)


urlpatterns = [
    path('admin-division-create/', AdminDivisionListCreateAPIView.as_view(), name='admin-division-create-api'),
    path('admin-division-list/', AdminDivisionListAPIView.as_view(), name='admin-division-list-api'),
    path('admin-division-retrieve-update-destroy/<int:id>', AdminDivisionRetrieveUpdateDestroyAPIView.as_view(), name='admin-division-retrieve-update-destroy-api'),

    path('admin-district-create/', AdminDistrictListCreateAPIView.as_view(), name='admin-districtn-create-api'),
    path('admin-district-list/',AdminDistrictListAPIView.as_view(), name='admin-district-list-api'),
    path('admin-district-retrieve-update-destroy/<int:id>', AdminDistrictRetrieveUpdateDestroyAPIView.as_view(), name='admin-district-retrieve-update-destroy-api'),

    #users
    path('users-division-list/', UsersDivisionListAPIView.as_view(), name='users-districtn-list-api'),
    path('users-district-list/',UsersDistrictListAPIView.as_view(), name='users-district-list-api'),
]