import  time

from channels.generic.websocket import JsonWebsocketConsumer


class TestWebsocketView(JsonWebsocketConsumer):
    
    def receive_json(self, content, **kwargs):
        """
        Called with decoded JSON content.
        """
        direction = content.get('direction', 'all')
        self.send_json(content={"test":123})
        while True:
            time.sleep(10)
            self.send_json(content={"test":123677})