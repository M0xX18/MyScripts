#!/usr/bin/env python3

import socket

def cliente():

    HOST = 'localhost'
    PORT = 1234

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with cliente as c:
        c.connect((HOST, PORT))
        
        while True:

            mensaje = input("Cliente: ")

            c.sendall(mensaje.encode())

            respuesta = c.recv(1024)

            print(f"Server: {respuesta.decode()}")

            if respuesta == b'Bye!':
                break

cliente()
