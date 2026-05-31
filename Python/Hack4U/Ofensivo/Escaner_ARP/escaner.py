#!/usr/bin/env python3

import argparse
import subprocess
import signal
import sys
import scapy.all as scapy
from termcolor import colored

import time

def def_handler(sig, frame):
    print(colored(f"\nSaliendo del programa...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Esta utilidad permite escanear dispositivos activos en una red usando ARP.")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")

    args = parser.parse_args()

    return args.target

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_packet = broadcast_packet/arp_packet

    answered, unanswered = scapy.srp(arp_packet, timeout=2, verbose=False)

    response = answered.summary()

    if response:
        print(response)

def main():
    target = get_arguments()
    scan(target)

if __name__ == "__main__":
    main()
