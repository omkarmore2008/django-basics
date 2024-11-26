"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumer import CustomWebsocketConsumer
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter(
    {        
        "http": get_asgi_application(),
        "websocket":  AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("ws/audio", CustomWebsocketConsumer.as_asgi()),
            ])
        )
    ),
    }
)
