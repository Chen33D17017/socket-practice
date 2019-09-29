import socket
from base import Socket_base

class Client(Socket_base):

    def init(self):
        self.socket_obj.connect((self.host, self.port))

def main():
    with Client(socket.gethostbyname('localhost'), 1234) as client:
        print(client.receive_msg())

if __name__ == '__main__':
    main()
