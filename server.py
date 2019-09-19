import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(10)
    client_socket, address = s.accept()
    print(f"Connect to {address} has been established")
    client_socket.send("Hello World".encode("utf-8"))
    s.close()


if __name__ == '__main__':
    main()
