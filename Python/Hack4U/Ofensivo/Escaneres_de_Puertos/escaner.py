#!/usr/bin/env python3

import socket
import argparse
import signal
import sys
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

open_sockets = []

def def_handler(sig, frame):
    print(colored(f"\nSaliendo...", "red"))

    for socket in open_sockets:
        socket.close()
        sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
    
def get_arguments():
    parser = argparse.ArgumentParser(description='TPC Port Escaner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target to scan")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan")
    options = parser.parse_args()

    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    open_sockets.append(s)

    return s

def port_scanner(port, host):
    
    s = create_socket()

    try:
        s.connect((host, port))
        s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
        response = s.recv(1024)
        response = response.decode(errors="ignore").split("\n")

        if response:
            print(colored(f"\nEl puerto {port} esta abierto\n", "green"))

            for line in response:
                print(f"{line}")

        else:
            print(colored(f"\nEl puerto {port} esta abierto", "green"))

    except(socket.timeout, ConnectionRefusedError):
        pass

    finally:
        s.close()

def scan_ports(ports, target):

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

def parse_ports(ports_str):
    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif ',' in ports_str:
        return map(int, ports_str.split(','))
    else:
        return (int(ports_str),)

def main():
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)

if __name__ == '__main__':
    main()
