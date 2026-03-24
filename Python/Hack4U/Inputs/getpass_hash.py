#!/usr/bin/env python3

from getpass import getpass
import hashlib

password = getpass("Introduce tu contraseña: ")

hash = hashlib.sha256(password.encode()).hexdigest()

print(f"Tu contraseña haseada es: {hash}")
