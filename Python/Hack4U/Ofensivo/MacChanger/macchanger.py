#!/usr/bin/env python3

import argparse
import re
import subprocess
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description="Esta utilidad permite cambiar la direccion Mac de una interfaz de red especifica")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="Nueva direccion Mac para la interfaz de red")

    return parser.parse_args()

def is_valid_input(interface, mac_address):
    
    is_valid_interface = re.match(r"^[e][n|t][s|h]\d{1,2}$", interface)
    is_valid_mac_address = re.match(r"^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$", mac_address)

    return is_valid_interface and is_valid_mac_address

def change_mac(interface, mac_address):
    
    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])

        print(f"\nLa direccion Mac ha sido cambiada correctamente!")

    else:
        print(colored("Argumentos invalidos", "red"))

def main():
    args = get_arguments()
    change_mac(args.interface, args.mac_address)

if __name__ == '__main__':
    main()
