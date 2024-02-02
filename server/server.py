import json
import asyncio
import ssl
import websockets

from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print("received", message)
        await websocket.send(f"echoing what client said: {message}")

async def main():
    print("Running server")
    async with serve(echo, "localhost", 3000):
        await asyncio.Future() 


asyncio.run(main())
        