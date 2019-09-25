import abc
import socket

class Socket_base(abc.ABC):
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.s_obj = None

    def __enter__(self):
        # create the socket
        # AF_INET == ipv4
        # SOCK_STREAM == TCP
        self.s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init()
        return self

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def send(self, receive_address, message):
        pass

    @abc.abstractmethod
    def receive(self):
        return self.s_obj.recv()

    def encrypt_message(self, msg):
        # TODO: add header for message
        msg.encode("utf-8")

    def decrypt_message(self, msg):
        # TODO: deal the message with header
        msg.encode("utf-8")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s_obj.close()

