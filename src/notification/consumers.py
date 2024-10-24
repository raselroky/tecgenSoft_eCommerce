from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.user = self.scope.get('user')
        if self.user.is_authenticated or not self.user.is_authenticated:
            self.group_name = f'user_{self.user.id}' 
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )
            await self.accept()
        else:
            print(f"User not authenticated: {self.user}")
            await self.close()

    async def disconnect(self, close_code):
       
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )

   
    async def receive(self, text_data):
        print(f"Received WebSocket message: {text_data}")  # Log the received data

        try:
            text_data_json = json.loads(text_data)  # Try parsing it as JSON
            message = text_data_json.get('message', '')

            if message:
                await self.send(text_data=json.dumps({
                    'message': message
                }))
            else:
                await self.send(text_data=json.dumps({
                    'error': 'Empty message received'
                }))
        except json.JSONDecodeError:
        # Send an error message back if JSON is invalid
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON format'
            }))

    async def notify(self, event):
        message = event.get('message', '')

        await self.send(text_data=json.dumps({
            'message': message
        }))

