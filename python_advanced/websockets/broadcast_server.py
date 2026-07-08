#!/usr/bin/env python3
""" Module implement broadcast communication """

import asyncio
import websockets

# Ensemble des clients actuellement connectés
connected_clients = set()


async def broadcast(message):
    """ send a message for all client """
    if connected_clients:
        # asyncio.gather permet d'envoyer à tout le monde
        # en parrallèle
        await asyncio.gather(
            *(client.send(message) for client in connected_clients),
            return_exceptions=True
        )


async def connection_handler(websocket):
    # Ajout du client qui se connecte
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            not_empty_message = message.strip()
            if not_empty_message == "":
                await websocket.send("ERR:EMPTY")
            else:
                await broadcast(f"B:{not_empty_message}")
    finally:
        # Si le client se déco ou à cause d'une erreur
        # on le retire
        connected_clients.remove(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
