from django.urls import path
from wishlist.views import UserWishlistListCreateAPIView,UserWislistListRetrieveUpdateDestroyAPIView

urlpatterns = [
    
     
     path('user-wishlist-create/',UserWishlistListCreateAPIView.as_view(),name='user-wishlist-item-create-list'),
     path('user-wishlist-retrieve-update-destroy/<int:id>',UserWislistListRetrieveUpdateDestroyAPIView.as_view(),name='user-wishlist-retrieve-update-destroy-api'),
]
