import asyncio
import websockets

CLIENTS = set()

async def start(websocket):
    # Add new client
    CLIENTS.add(websocket)
    print(f"[CONNECTED] {websocket.remote_address}")
    print(f"Current clients: {[ws.remote_address for ws in CLIENTS]}")
    #look for messages on the server and only send messages to clients that are not the sender
    try:
        async for message in websocket:
            for client in CLIENTS:
                if client != websocket:
                    await client.send(message)
#if the client closes out then notify server the client disconnected
    except websockets.exceptions.ConnectionClosed:
        print(f"[DISCONNECTED] {websocket.remote_address}")
#remove client from client list and notify server of remaining clients
    finally:
        CLIENTS.remove(websocket)
        print(f"Remaining clients: {[ws.remote_address for ws in CLIENTS]}")
#starter code for running server
async def main():
    async with websockets.serve(start, "localhost", 8080):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
