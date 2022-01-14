from .templates import templates
from typing import Type, Callable, Optional, Union

from pincer import Client, command, ChatCommandHandler
from pincer.commands import Group, Subgroup
from pincer.objects import ThrottleScope

TC = Type[Client]


def guild_command(guild: int):
    def decorator(
            func=None,
            *,
            name: Optional[str] = None,
            description: Optional[str] = "Description not set",
            enable_default: Optional[bool] = True,
            cooldown: Optional[int] = 0,
            cooldown_scale: Optional[float] = 60.0,
            cooldown_scope: Optional[ThrottleScope] = ThrottleScope.USER,
            parent: Optional[Union[Group, Subgroup]] = None
    ):
        return command(
            func=func,
            name=name,
            description=description,
            enable_default=enable_default,
            guild=guild,
            cooldown=cooldown,
            cooldown_scale=cooldown_scale,
            cooldown_scope=cooldown_scope,
            parent=parent
        )

    return decorator


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
