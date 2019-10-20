import socket
import sys
import errno
from base import Socket_base

class Client(Socket_base):

    def init(self):
        self.username = input("ENTER YOUR NAME: ")
        self.socket_obj.connect((self.host, self.port))
        self.socket_obj.setblocking(False)
        self.send_msg(self.socket_obj, self.username)

    def start(self):
        while True:
            msg = input(f"{self.username}: ")
            self.send_msg(self.socket_obj, msg)
            try:
                msg = self.receive_msg(self.socket_obj)
                if msg:
                    print(msg)
                else:
                    continue

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error', str(e))
                    sys.exit()
                continue

            except Exception as e:
                print("General error ", str(e))
                sys.exit()

def main():
    with Client(socket.gethostbyname('localhost'), 1234) as client:
        client.start()

if __name__ == '__main__':
    main()
