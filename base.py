import abc
import socket

class Socket_base(abc.ABC):
    HEADER_SIZE = 10
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __enter__(self):
        # create the socket
        # AF_INET == ipv4
        # SOCK_STREAM == TCP
        self.init()
        return self

    @abc.abstractmethod
    def init(self):
        return NotImplementedError

    def send_msg(self, destination_socket, msg):
        msg_with_header = f"{len(msg):<{self.HEADER_SIZE}}{msg}"
        destination_socket.send(msg_with_header.encode("utf-8"))

    def receive_msg(self, object_socket):
        try:
            msg_header = object_socket.recv(self.HEADER_SIZE)
            if not msg_header:
                return False
            msg_length = int(msg_header.strip())
            msg = ""
            while True:
                if len(msg) == msg_length:
                    return msg
                else:
                    msg += object_socket.recv(16).decode("utf-8")
        except:
            return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket_obj.close()

