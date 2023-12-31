from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QMainWindow

from client.uiforms.mainform import Ui_MainWindow
from common.config import EventNames
from common.utils import EventBus


class MainAppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.eventBus = EventBus.instance()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.post_message)
        self.sendButton.setShortcut(QKeySequence("CTRL+S"))
        self.CancelButton.clicked.connect(self.quit)
        self.app = app
        self.register()

    def closeEvent(self, event):
        self.eventBus.emit(event_name=EventNames.EN_NET_CLOSE, event="")
        event.accept()

    def register(self):
        self.eventBus.add_listener(event_name=EventNames.EN_FROM_NET, listener=self.receive_message)
        self.eventBus.add_listener(event_name=EventNames.EN_UI_CLOSE, listener=self.quit)

    def post_message(self):
        self.eventBus.emit(event_name=EventNames.EN_FROM_UI, event=self.message.toPlainText())
        self.message.clear()

    async def receive_message(self, event):
        self.MessagesListWidget.addItem(event)
        # await asyncio.sleep(0.0001)

    async def quit(self, event):
        self.MessagesListWidget.addItem("Disconnected.You must quit from application")
        # self.destroy(destroyWindow=True)
