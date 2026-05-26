#/!usr/bin/env python3

import socket
import threading

def client_thread(client_socket, clients, usernames):

    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    print(f"\nEl usuario {username} se ha conectado")

def server():

    HOST = 'localhost'
    PORT = 1811

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Esperando conexiones")

    clients = []
    usernames = {}

    while True:

        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        print(f"Nuevo cliente conectado: {address}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

    server_socket.close()

if __name__ == '__main__':
    server()
