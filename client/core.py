import traceback
from socket import socket, AF_INET, SOCK_STREAM

from common.config import EventNames
from common.utils import EventBus


class ClientClass:
    def __init__(self, host, port):
        self.eventBus = EventBus.instance()
        self.register()
        self.BUFFSIZE = 1024
        self.ADDR = (host, port)
        self.CLIENT = socket(AF_INET, SOCK_STREAM)
        self.CLIENT.connect(self.ADDR)
        self.ami_closed = False

    def register(self):
        self.eventBus.add_listener(event_name=EventNames.EN_FROM_UI, listener=self.send)
        self.eventBus.add_listener(event_name=EventNames.EN_NET_CLOSE, listener=self.quit)
        print("registered NET receiver")

    async def send(self, event):
        if not self.ami_closed:
            try:
                msg = event
                print(f"send:{msg}")
                self.CLIENT.send(bytes(msg, "utf8"))
                if msg == "[quit]":
                    self.ami_closed = True
                    self.CLIENT.close()
            except:
                print(f"Error:{traceback.format_exc()}")
                self.CLIENT.close()

    def receive(self):
        while True:
            try:
                if not self.ami_closed:
                    msg = self.CLIENT.recv(self.BUFFSIZE).decode("utf8")
                    print(f"receive:{msg}")
                    self.eventBus.emit(event_name=EventNames.EN_FROM_NET, event=msg)
                else:
                    self.eventBus.emit(event_name=EventNames.EN_UI_CLOSE, event="")
                    self.CLIENT.close()
                    break
            except OSError:
                print(f"Error:{traceback.format_exc()}")
                self.CLIENT.close()
                break

    async def quit(self, event):
        self.CLIENT.close()
