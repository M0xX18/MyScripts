#!/usr/bin/env python3

import os
import time

path = os.getcwd()

print(f"La carpeta actual es: {path}")

print("Listando los directorios de esta carpeta...")

time.sleep(1)

files = os.listdir()

for file in files:
    print(file)

file = input("\nDigite el nombre del archivo que desea validar o crear con su respectiva extension: ")

print(f"\nValidando si {file} existe...")

file_exist = os.path.exists(file)

time.sleep(1)

if file_exist:
    print(f"\nSi, el archivo {file} existe")
else:
    print(f"\nNo, creando {file}...")
    time.sleep(1)
    with open(file, 'a'):
        pass
    print(f"\n{file} creado correctamente!")

env = os.getenv('TERM')

print(f"\nEste dispositivo esta usando la terminal:\n {env}")
