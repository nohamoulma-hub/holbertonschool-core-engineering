#!/usr/bin/env python3
"""
Integrate WebSocket communication
into a web-facing Python application
"""

from starlette.applications import Starlette # type: ignore
from starlette.responses import HTMLResponse # type: ignore
from starlette.routing import Route, WebSocketRoute # type: ignore

async def homepage(request):
    return HTMLResponse("<h1>WebSocket App</h1>")

async def websocket_endpoint(websocket):
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
