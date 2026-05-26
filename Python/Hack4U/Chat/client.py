#!/usr/bin/env python3

import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def client_program():

    HOST = 'localhost'
    PORT = 1811

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    username = input(f"Digita tu nombre de usuario: ")

    client_socket.sendall(username.encode())

if __name__ == '__main__':
    client_program()
