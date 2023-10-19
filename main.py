# This is a sample Python script.
import sys
from threading import Thread

from PyQt6 import QtWidgets

from common import config
from common.config import host, port
from common.utils import EventBus
from appserver.core import MessageSever
from client.core import ClientClass
from client.presentation import MainAppWindow


def init_server():
    server = MessageSever(config.host, config.port)
    server.start()
    accept_thread = Thread(target=server.listener)
    accept_thread.start()
    accept_thread.join()
    server.stop()


def init_client():
    client_class = ClientClass(host=host, port=port)
    client_thread = Thread(target=client_class.receive)
    client_thread.start()


if __name__ == '__main__':
    arguments = sys.argv
    eventBus = EventBus.instance()
    if arguments.__contains__("server"):
        init_server()
    if arguments.__contains__("client"):
        app = QtWidgets.QApplication(list())
        windowClass = MainAppWindow(app)
        windowClass.show()
        init_client()
        sys.exit(app.exec())
