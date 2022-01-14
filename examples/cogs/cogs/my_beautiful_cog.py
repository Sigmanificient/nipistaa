from pincer import command
from pincer.objects import Embed, MessageContext

import nipistaa
from nipistaa.templates import ping
from ..config import GUILD_ID


@nipistaa.hook(ping, guild=GUILD_ID)
class MyBeautifulCog:

    # your own commands
    @command
    async def say(self, ctx: MessageContext, message: str):
        return Embed(description=f"{ctx.author.user.mention} said:\n{message}")


setup = MyBeautifulCog
