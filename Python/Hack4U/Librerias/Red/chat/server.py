#!/usr/bin/env python3

import socket

def server():

    HOST = 'localhost'
    PORT = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))

        s.listen()

        conn, addr = s.accept()
        
        with conn:
        
            data = conn.recv(1024)

            print(f"Cliente: {data.decode()}")

            primer_mensaje = b'Hola! bienvenido en que te ayudo?'

            conn.sendall(primer_mensaje)
            
            while True:

                data = conn.recv(1024)

                print(f"Cliente: {data.decode()}")

                mensaje = input("Server: ")

                if mensaje == b'Bye!':
                    break

                conn.sendall(mensaje.encode())

server()
