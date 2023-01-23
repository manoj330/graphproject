from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from testapp import consumers
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
# websocket_urlPattern=[
#     path('ws/polData',consumers.graphconsumers),
# ]
ws_url_patterns=[
    path('ws/polData/',consumers.graphconsumers.as_asgi()),
                                                  ]                                                       
