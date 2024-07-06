from django.urls import path,include
from user.views import UserListCreateAPIView,login_with_password,logout,refreshed_token

urlpatterns=[
    path('signup/',UserListCreateAPIView.as_view(),name='user-create-api'),
    path('login/',login_with_password,name='login-users'),
    path('logout/',logout,name='logout-users'),
    path('refresh-token/',refreshed_token,name='refresh-token-users'),
]