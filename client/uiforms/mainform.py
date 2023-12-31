# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.MessagesListWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.MessagesListWidget.setObjectName("MessagesListWidget")
        self.horizontalLayout_2.addWidget(self.MessagesListWidget)
        self.contactListWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.contactListWidget.setObjectName("contactListWidget")
        self.horizontalLayout_2.addWidget(self.contactListWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.message = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sendButton = QtWidgets.QPushButton(parent=self.centralwidget)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.sendButton.setIcon(icon)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.CancelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        icon = QtGui.QIcon.fromTheme("go-jump")
        self.CancelButton.setIcon(icon)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Messenger"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.CancelButton.setText(_translate("MainWindow", "Reconnect"))
