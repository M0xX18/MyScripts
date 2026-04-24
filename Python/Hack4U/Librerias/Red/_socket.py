#!/usr/bin/env python3

import socket

def start():

    host = 'localhost'
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with server as s:
        s.bind((host, port))
        print(f"Servidor\nHOST: {host}\nPORT: {port}\n")
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            print(f"Cliente {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                s.sendall(data)
start()
