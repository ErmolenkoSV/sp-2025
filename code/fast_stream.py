import asyncio

from faststream import FastStream
from faststream.redis import RedisBroker


broker = RedisBroker("redis://localhost:6379")
app = FastStream(broker)

@broker.subscriber("in-channel")
@broker.publisher("out-channel")
async def handle_msg(user: str) -> str:
    return f"Hello: {user} user"


@broker.subscriber("out-channel")
async def handle_msg_2(message: str) -> str:
    return f"Hello user"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.start())
    loop.run_forever()
    