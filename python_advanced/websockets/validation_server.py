#!/usr/bin/env python3
""" Module add a basic message validation """

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    async for message in websocket:
        try:
            # strip retire les espaces au début et à la fin
            not_empty_message = message.strip()
            if not_empty_message == "":
                await websocket.send("ERR:EMPTY\n")
            else:
                await websocket.send(f"OK:{message}")
        except ConnectionClosed:
            pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
