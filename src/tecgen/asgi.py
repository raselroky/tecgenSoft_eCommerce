import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from notification.routing import websocket_urlpatterns
from channels.security.websocket import AllowedHostsOriginValidator
from notification.consumers import NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecgen.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})