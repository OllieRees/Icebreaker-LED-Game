import websockets
import asyncio
from gameLogic import iceBreaker
from threading import Thread

class websocketComms(Thread):

    def __init__(self):
        self.game = iceBreaker()
        Thread.__init__(self)

    async def consumer_handler(self, websocket, path):
        async for message in websocket:
            response = self.game.processMessage(message)
            await websocket.send(response)

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        start_server = websockets.serve(self.consumer_handler, 'localhost', 6362)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()