import socket

HOST = ('localhost', 10000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(HOST)
server_socket.listen()

print('I am listening your connections😈')

while True:
    client_socket, addr = server_socket.accept()
    print('Connected -', addr)

    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = b"Hello my friend!"  # encode(fmt)
            client_socket.send(response)

    print('Outside inner while loop!')
    client_socket.close()
