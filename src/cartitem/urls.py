from django.urls import path,include
from cartitem.views import (
    UserCartItemListCreateAPIView,UserCartItemListRetrieveUpdateDestroyAPIView
    )


urlpatterns=[

    path('users-cart-create/',UserCartItemListCreateAPIView.as_view(),name='user-cart-create-api'),
    path('users-cart-retrieve-update-destroy/<int:id>',UserCartItemListRetrieveUpdateDestroyAPIView.as_view(),name='user-cart-retrieve-update-destroy-api'),


]