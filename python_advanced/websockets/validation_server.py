#!/usr/bin/env python3
""" Module add a basic message validation """

import asyncio
import websockets


async def connection_handler(websocket):
    async for message in websocket:
        # strip retire les espaces au début et à la fin
        trimmed = message.strip()
        if trimmed == "":
            await websocket.send("ERR:EMPTY\n")
        else:
            await websocket.send(f"OK:{trimmed}\n")


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
