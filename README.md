# Nipistaa

A pincer library that provides templates commands for the [Pincer](https://github.com/pincer-org/pincer) API wrapper.

## Usage example

```py
import nipistaa
from nipistaa.templates import ping
from pincer import Client

@nipistaa.hook(ping, guild=1234567890)
class Bot(Client):

    @Client.event
    async def on_ready(self):
        print('Logged in as', self.bot)


if __name__ == '__main__':
    Bot('...').run()
```

> or even make it with bare python Client!
```py
import nipistaa
from pincer import Client

Bot = nipistaa.hook('ping', guild=1234567890)(Client)
Bot('...').run()
```

> want to use nipistaa withing a Cog? No problem.

```py
from pincer import command
from pincer.objects import Embed, MessageContext

import nipistaa
from nipistaa.templates import ping


@nipistaa.hook(ping, guild=134567890)
class MyBeautifulCog:

    # your own commands
    @command
    async def say(self, ctx: MessageContext, message: str):
        return Embed(description=f"{ctx.author.user.mention} said:\n{message}")


setup = MyBeautifulCog
```
