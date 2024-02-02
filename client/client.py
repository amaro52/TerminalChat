import websocket
import _thread
import time
import rel
import asyncio

def on_message(ws, message):
    print(f">>> {message}")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

async def on_open(ws):
    message = input('message: ')
    ws.send(message)


async def main():
    ws = websocket.WebSocketApp("ws://localhost:3000",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

asyncio.run(main())