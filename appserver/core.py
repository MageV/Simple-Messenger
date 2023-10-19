import traceback
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

import stun


class MessageSever:
    def __init__(self, host, port):
        self.clients = {}
        self.adresses = {}
        self.HOST = host
        self.PORT = port
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)

    def start(self):
        self.SERVER.listen(5)

    def stop(self):
        self.SERVER.close()

    def listener(self):
        while True:
            client, client_addr = self.SERVER.accept()
            print(f"{client_addr} connection accepted")
            client.send(bytes("Hello! Put your name and press Ctrl+S", "utf8"))
            self.clients.update({client: client_addr})
            Thread(target=self.client_sessions, args=(client,)).start()

    def client_sessions(self, client):
        name = client.recv(self.BUFSIZE).decode("utf8")
        welcome = f"Welcome {name}.\n To quit from chat enter [quit]"
        client.send(bytes(welcome, "utf8"))
        msg = f"{name} entered chat"
        self.broadcast(bytes(msg, "utf8"))
        while True:
            msg = client.recv(self.BUFSIZE)
            if msg != bytes("[quit]", "utf8"):
                self.broadcast(msg, prefix=name)
            else:
                client.send(bytes("[quit]", "utf8"))
                self.clients.pop(client)
                self.broadcast(bytes(f"{name} has left chat", "utf8"))
                client.close()
                break

    def broadcast(self, msg, prefix=""):
        for sock in self.clients:
            try:
                sock.send(bytes(prefix + ":", "utf8") + msg)
            except BrokenPipeError:
                print(f"Error:{traceback.format_exc()}")
                self.stop()
