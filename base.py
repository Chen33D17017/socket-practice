import abc
import socket

class Socket_base(abc.ABC):
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def __enter__(self):
        self.s_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init()
        return self

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def send(self):
        pass

    @abc.abstractmethod
    def receive(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s_obj.close()
        
if __name__ == '__main__':
    print('Hello World')
