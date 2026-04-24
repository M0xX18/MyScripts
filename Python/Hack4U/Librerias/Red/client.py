#!/usr/bin/env python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('localhost', 1234)
client.connect(server)

try:
    message = b"Hola! Esta es una prueba"
    client.sendall(message)
    data = client.recv(1024)

    print(f"Servidor: {data.decode()}")
finally:
    client.close()
