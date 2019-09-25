import socket
from base import Socket_base

class Server(Socket_base):
    def __init__(self, ip_address, port):
        Socket_base.__init__(self, ip_address, port)
        # logs for connection
        self.connected_list = []

    def init(self):
        self.s_obj.bind((socket.gethostname(), self.port))
        self.s_obj.listen(5)

    def build(self):
        pass
        #TODO: implement the server's listening


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket, address = s.accept()
    print(f"Connect to {address} has been established")
    client_socket.send("Hello World".encode("utf-8"))
    s.close()


if __name__ == '__main__':
    main()
