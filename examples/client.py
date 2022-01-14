import nipistaa
from pincer import Client

GUILD_ID: int = ...
TOKEN: str = ...

Bot = nipistaa.hook('ping', guild=GUILD_ID)(Client)
Bot(TOKEN).run()
