import socket
from base import Socket_base

class Server(Socket_base):
    def __init__(self, ip_address, port):
        Socket_base.__init__(self, ip_address, port)
        # logs for connection
        self.connected_list = []

    def init(self, listen_number=5):
        self.socket_obj.bind((socket.gethostbyname('localhost'), 1234))
        self.socket_obj.listen(listen_number)

    def build(self):
        pass
        # client_socket, address = self.socket_obj.accept()
        # self.connected_list.append((client_socket, address))

def main():
    with Server(socket.gethostbyname('localhost'), 1234) as server:
        client_socket, address = server.socket_obj.accept()
        print(f"Connect to {address} has been established")
        server.connected_list.append((client_socket, address))
        for client_socket, address in server.connected_list:
            print("send message")
            server.send_msg(client_socket, "Hello Word")




if __name__ == '__main__':
    main()
