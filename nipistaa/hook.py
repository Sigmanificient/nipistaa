from typing import Callable, Optional, Union

from pincer import Client, command, ChatCommandHandler
from pincer.commands import Group, Subgroup
from pincer.objects import ThrottleScope

from .templates import templates
from .utils import TC
from .utils.guild_command import guild_command


def hook(
    *commands,
    guild: Optional[int]
) -> Callable[[TC], TC]:
    _command = guild_command(guild) if guild else command

    def wrapper(cls: TC) -> TC:
        for cmd in commands:
            if cmd in templates.keys():
                cmd = templates[cmd]

            setattr(cls, cmd.__name__, _command(cmd))

            if isinstance(cls, Client):
                _old_run = cls.run
                setattr(cls, 'run', run_wrapper(_old_run))

        return cls

    return wrapper


def run_wrapper(_old_run):
    def run(self, *args, **kwargs):
        ChatCommandHandler.managers['nipistaa.hook'] = self
        _old_run(self, *args, **kwargs)

    return run
