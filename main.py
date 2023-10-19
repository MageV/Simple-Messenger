# This is a sample Python script.
import sys
from threading import Thread

from PyQt6 import QtWidgets

from app_config import config
from app_config.config import host, port
from app_config.utils import EventBus
from appserver.core import MessageSever
from client.core import ClientClass
from client.presentation import mainAppWindow


def init_server():
    server = MessageSever(config.host, config.port)
    server.start()
    ACCEPT_THREAD = Thread(target=server.listener)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.stop()


def init_client():
    clientClass = ClientClass(host=host, port=port)
    client_thread = Thread(target=clientClass.receive)
    client_thread.start()




if __name__ == '__main__':
    arguments = sys.argv
    eventBus = EventBus.instance()
    if arguments.__contains__("server"):
        init_server()
    if arguments.__contains__("client"):
        app = QtWidgets.QApplication(list())
        windowClass = mainAppWindow(app)
        windowClass.show()
        init_client()
        sys.exit(app.exec())


