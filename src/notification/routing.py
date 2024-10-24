from django.urls import path
from notification import consumers
from django.urls import re_path

websocket_urlpatterns = [
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
]
