from .views import AdminNotificationListAPIView,AdminNotificationRetrieveDestroyAPIView,UsersNotificationListAPIView,UsersNotificationRetrieveAPIView
from django.urls import path

urlpatterns=[
    path('admin-notification/',AdminNotificationListAPIView.as_view(),name='admin-notifcation-list'),
    path('admin-notification-retrieve-update-destroy/<int:id>',AdminNotificationRetrieveDestroyAPIView.as_view(),name='admin-notifcation-retrieve-destroy'),

    path('users-notification/',UsersNotificationListAPIView.as_view(),name='notifcation-list'),
    path('users-notification-retrieve/<int:id>',UsersNotificationRetrieveAPIView.as_view(),name='notifcation-retrieve-destroy'),
]