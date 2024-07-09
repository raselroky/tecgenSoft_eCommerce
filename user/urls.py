from django.urls import path,include
from user.views import UserListCreateAPIView,login_with_password,logout,refreshed_token

urlpatterns=[
    path('signup/',UserListCreateAPIView.as_view(),name='user-create-api'),
    path('login/',login_with_password.as_view(),name='login-users'),
    path('logout/',logout.as_view(),name='logout-users'),
    path('refresh-token/',refreshed_token.as_view(),name='refresh-token-users'),
]