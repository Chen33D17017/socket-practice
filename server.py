import socket
from base import Socket_base
import select

class Server(Socket_base):
    def __init__(self, ip_address, port):
        Socket_base.__init__(self, ip_address, port)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.connected_list = [self.socket_obj]
        self.connected_list = [self.socket_obj]
        self.clients = {}

    def init(self, listen_number=5):
        self.socket_obj.bind((socket.gethostbyname('localhost'), 1234))
        self.socket_obj.listen(listen_number)

    def socket_remove(self, target_socket):
        if target_socket not in self.connected_list:
            raise ValueError("USER NOT EXIST IN LIST")
        else:
            self.connected_list.remove(target_socket)
            del self.clients[target_socket]

    def build(self):
        while True:
            read_sockets, _ , exception_sockets = select.select(self.connected_list, [], self.connected_list)
            for notified_socket in read_sockets:
                # If the notified socket is server socket
                if notified_socket == self.socket_obj:
                    client_socket, client_address = self.socket_obj.accept()
                    user = self.receive_msg(client_socket)
                    if user == False:
                        continue
                    self.clients[client_socket] = user
                    self.connected_list.append(client_socket)
                    print(f"{user} in {client_address} is login")
                # If the notified socket is client socket
                else:
                    msg = self.receive_msg(notified_socket)
                    # If the client is disconnected
                    if msg == False:
                        print('Closed connection from: {}'.format(self.clients[notified_socket]))
                        self.socket_remove(notified_socket)
                        continue
                    # Get message from client
                    else:
                        user = self.clients[notified_socket]
                        print(f"receive {msg} from {user}")
                        # Sending the message to other user
                        for client_socket in self.connected_list:
                            if client_socket == notified_socket or client_socket == self.socket_obj :
                                continue
                            else:
                                self.send_msg(client_socket, f"{user} : {msg}")
            for err_socket in exception_sockets:
                self.socket_remove(err_socket)
def main():
    with Server(socket.gethostbyname('localhost'), 1234) as server:
        server.build()

if __name__ == '__main__':
    main()
