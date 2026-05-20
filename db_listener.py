import asyncio
import asyncpg

async def handle_notification(connection, pid, channel, payload):
    print("📡 Real-time update received:")
    print(payload)


async def listen():
    conn = await asyncpg.connect(
        user='postgres',
        password='postgres123',
        database='apt_realtime',
        host='localhost',
        port=5433   # IMPORTANT (your port)
    )

    await conn.add_listener('order_channel', handle_notification)

    print("🚀 Listening for database changes...")

    while True:
        await asyncio.sleep(1)


asyncio.run(listen())