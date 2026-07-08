#!/usr/bin/env python3
""" Module add a basic message validation """

import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        trimmed = message.strip()
        if trimmed == "":
            await websocket.send("ERR:EMPTY\n")
        else:
            await websocket.send(f"OK:{trimmed}\n")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
