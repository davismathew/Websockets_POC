from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from test_app.consumers import TestWebsocketView

application = ProtocolTypeRouter({

    # WebSocket service handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url("test/", TestWebsocketView),
        ])
    ),
})