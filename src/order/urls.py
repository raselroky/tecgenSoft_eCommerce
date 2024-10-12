from django.urls import path
from .views import (
    UserOrderCreateListCreateAPIView
)


urlpatterns = [
    path('user-order-create/', UserOrderCreateListCreateAPIView.as_view(),name='user-order-create'),
    
]