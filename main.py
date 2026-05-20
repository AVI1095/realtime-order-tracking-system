import asyncio
import asyncpg
import json
from fastapi import FastAPI, WebSocket

app = FastAPI()

clients = {}


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    clients[username] = websocket
    print(f"{username} connected")

    try:
        while True:
            await websocket.receive_text()
    except:
        clients.pop(username, None)
        print(f"{username} disconnected")


async def notify_clients(payload):
    data = json.loads(payload)

    user = data.get("customer_name")

    if user in clients:
        try:
            await clients[user].send_text(payload)
        except:
            clients.pop(user, None)


async def handle_notification(connection, pid, channel, payload):
    print("Sending:", payload)
    await notify_clients(payload)


async def listen_db():
    conn = await asyncpg.connect(
        user='postgres',
        password='postgres123', 
        database='apt_realtime',
        host='localhost',
        port=5433
    )

    await conn.add_listener('order_channel', handle_notification)

    print("Listening to DB...")

    while True:
        await asyncio.sleep(1)


@app.on_event("startup")
async def startup():
    asyncio.create_task(listen_db())
