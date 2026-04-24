#!/usr/bin/env python3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 1234)

server.bind(address)

server.listen(1)

while True:
    client_socket, client_address = server.accept()
    data = client_socket.recv(1024)

    print(f"[{client_address}]: {data.decode()}")

    enviar = input("Enviar: ")

    client_socket.sendall(f"{enviar}".encode())

    pass
