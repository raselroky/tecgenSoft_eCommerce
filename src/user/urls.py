from django.urls import path,include
from user.views import *

urlpatterns=[
    path('signup/',UserListCreateAPIView.as_view(),name='user-create-api'),
    path('signin/',Login.as_view(),name='login-users'),
    path('logout/',Logout.as_view(),name='logout-users'),
    path('forgetpassword/',ForgetPassword.as_view(),name='forget_password-users'),
    #path('logouts/',obtain_auth_token,name='logout-users'),
    
    #path('refresh-token/',refreshed_token.as_view(),name='refresh-token-users'),
    path('refresh-token/', RefreshTokenAPIView.as_view(), name='token_refresh'),

    path('userget/<str:id>', UserGetRetrieve.as_view(), name="user-get"),
    path('user-list/', UserListAPIView.as_view(), name="user-list"),
    path('role-create/', RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('role-retrieve-update-destroy/<int:id>',RoleRetrieveUpdateDestroyAPIView.as_view(), name='role-retrieve-update-destroy'),

    path('permission-list/', PermissionListAPIView.as_view(), name='permission-list-api'),

    path('role-permissions/', RolePermissionsListCreateView.as_view(), name='role-permissions-list-create'),
    path('role-permissions-list/', RolePermissionsListAPIView.as_view(), name='role-permissions-list'),
    path('role-permissions/<int:id>', RolePermissionsRetrieveUpdateDestroyView.as_view(), name='role-permissions-detail'),
    path('role-permissions-check/', RolePermissionsSearchCheckAPIView.as_view(), name='role-permissions-check-api'),

    path('role-update-destroy/<int:id>', RolesRetrieveUpdateDestroy.as_view(), name='role-update-destroy-detail'),

]