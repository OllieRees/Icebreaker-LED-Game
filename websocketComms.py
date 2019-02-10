import websockets
import asyncio
from gameLogic import iceBreaker
from threading import Thread

class websocketComms(Thread):

    def __init__(self, ib):
        self.game = ib
        Thread.__init__(self)

    def processMessage(self, message):
        pass

    async def consumer_handler(self, websocket, path):
        async for message in websocket:
            print(message)
            
            response = self.game.processMessage(message)

            if response[0] == 'host':
                self.processMessage(response[1])
            else:
                await websocket.send(response[1])

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        start_server = websockets.serve(self.consumer_handler, 'localhost', 63636)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()