from enum import Enum, auto

host = "127.0.0.1"
port = 30333


class EventNames(Enum):
    EN_FROM_NET = auto()
    EN_FROM_UI = auto()
    EN_UI_CLOSE = auto()
    EN_NET_CLOSE = auto()
