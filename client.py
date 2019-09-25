import socket
from base import Socket_base

class Client(Socket_base):

    def init(self):
        self.s_obj.connect((socket.gethostname(), self.port))

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    full_msg = ''
    while True:
        msg = s.recv(10)
        if len(msg) == 0:
            break
        full_msg += msg.decode("utf-8")
    print(full_msg)


if __name__ == '__main__':
    main()
