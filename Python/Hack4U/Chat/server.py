#/!usr/bin/env python3

import socket
import threading

def server():

    HOST = 'localhost'
    PORT = 1811

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Esperando conexiones")

    clients = []
    username = {}

    while True:


if __name__ == '__main__':
    server()
