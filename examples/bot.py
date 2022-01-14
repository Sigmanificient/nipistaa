import nipistaa
from nipistaa.templates import ping
from pincer import Client

GUILD_ID: int = ...
TOKEN: str = ...


@nipistaa.hook(ping, guild=GUILD_ID)
class Bot(Client):

    @Client.event
    async def on_ready(self):
        print('Logged in as', self.bot)


if __name__ == '__main__':
    Bot(TOKEN).run()
