import socket
from base import Socket_base

class Server(Socket_base):
    def init(self):
        pass

    def build(self):
        pass


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket, address = s.accept()
    print(f"Connect to {address} has been established")
    client_socket.send("Hello World".encode("utf-8"))
    s.close()


if __name__ == '__main__':
    main()
