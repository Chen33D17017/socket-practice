import abc
import socket

class Socket_base(abc.ABC):
    HEADER_SIZE = 10
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_obj = None

    def __enter__(self):
        # create the socket
        # AF_INET == ipv4
        # SOCK_STREAM == TCP
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init()
        return self

    @abc.abstractmethod
    def init(self):
        pass

    def send_msg(self, destination_socket, msg):
        msg_with_header = f"{len(msg):<{self.HEADER_SIZE}}{msg}"
        destination_socket.send(msg_with_header.encode("utf-8"))

    def receive_msg(self):
        new_msg = True
        msg_size = 0
        msg = ""
        while True:
            receive_msg = self.socket_obj.recv(16).decode("utf-8")
            if new_msg :
                msg_size = int(receive_msg[:self.HEADER_SIZE])
                msg += receive_msg[self.HEADER_SIZE:]
                new_msg = False
            else :
                msg += receive_msg
            if msg_size == len(msg):
                return msg


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket_obj.close()

