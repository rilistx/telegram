# This is Client

import socket

HOST = ('localhost', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connect to', HOST)

message = client.recv(1024)
print(message.decode('UTF-8'))
