from typing import Optional, Union

from pincer import command
from pincer.commands import Subgroup, Group
from pincer.objects import ThrottleScope


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
