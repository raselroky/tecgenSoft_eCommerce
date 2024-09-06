from django.urls import path,include
from user.views import UserListCreateAPIView,Login,Logout,ForgetPassword

urlpatterns=[
    path('signup/',UserListCreateAPIView.as_view(),name='user-create-api'),
    path('signin/',Login.as_view(),name='login-users'),
    path('logout/',Logout.as_view(),name='logout-users'),
    path('forgetpassword/',ForgetPassword.as_view(),name='forget_password-users'),
    #path('logouts/',obtain_auth_token,name='logout-users'),
    
    #path('refresh-token/',refreshed_token.as_view(),name='refresh-token-users'),

]