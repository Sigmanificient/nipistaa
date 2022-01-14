async def ping() -> str:
    return 'pong!'


async def hello_world() -> str:
    return 'Hello World!'


async def say(message: str) -> str:
    return message


templates = {
    'ping': ping,
    'hello_world': hello_world,
    'say': say
}
