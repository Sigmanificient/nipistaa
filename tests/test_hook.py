import nipistaa
from pincer import Client


def test_not_hook():
    assert 'ping' not in dir(Client)


def test_hook():
    _Client = nipistaa.hook('ping', guild=0)(Client)
    assert 'ping' in dir(_Client)
