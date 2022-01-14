# Nipistaa

![Lines of code](https://tokei.rs/b1/github/Sigmanificient/nipistaa?category=code&path=nipistaa)
![Repo Size](https://img.shields.io/github/repo-size/Sigmanificient/nipistaa)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/nipistaa)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Sigmanificient/nipistaa?label=commits)
![Discord](https://img.shields.io/discord/881531065859190804)
[![codecov](https://codecov.io/gh/Sigmanificient/nipistaa/branch/main/graph/badge.svg?token=XF58SIO83F)](https://codecov.io/gh/Sigmanificient/nipistaa)
![gitmoji](https://img.shields.io/badge/gitmoji-%20🚀%20💀-FFDD67.svg)

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
[file](/examples/bot.py)

<br>

> or even make it with bare python Client!
```py
import nipistaa
from pincer import Client

Bot = nipistaa.hook('ping', guild=1234567890)(Client)
Bot('...').run()
```
[file](/examples/client.py)

<br>

> want  to use nipistaa withing a Cog? No problem.

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
[file](/examples/cogs/bot.py)
