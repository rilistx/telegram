# This is Server

import socket

HOST = ('localhost', 10000)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(HOST)
server.listen()

print('I am listening your connections😈')

while True:
    connection, addr = server.accept()
    print('Connected -', addr)
    response = b"Hello my friend!"  # encode(fmt)
    connection.send(response)

    connection.close()
