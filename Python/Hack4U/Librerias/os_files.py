#!/usr/bin/env python3

import os
import time
import shutil

print("- El archivo existe?")
time.sleep(1)

if os.path.exists("text.txt"):
    print("+ Si existe")
else:
    with open("text.txt", "w") as file:
        file.write("Efectivamente, si existo!")
    print("+ No... pero ahora si :D")

time.sleep(1)
print("- Pero existe la carpeta correcta?")
time.sleep(1)

if os.path.exists("carpeta_correcta/dentro_de_carpeta_correcta"):
    print("+ Si, todo esta bien!")
else:
    print("+ No, todo mal...")
    os.makedirs("carpeta_correcta/dentro_de_carpeta_correcta")
    # os.mkdir("carpeta_correcta")
    # os.mkdir("carpeta_correcta/dentro_de_carpeta_correcta")
    print("+ Pero ya la cree!")

time.sleep(1)
print("- Bueno el archivo esta dentro de la carpeta?")
time.sleep(1)

if os.path.exists("carpeta_correcta/text.txt"):
    print("+ Todo esta perfecto!")
else:
    carpeta = os.path.join("carpeta_correcta", "dentro_de_carpeta_correcta")
    shutil.move("text.txt", f"{carpeta}/text.txt")
    print("+ Ya la movi por ti... de nada")

time.sleep(1)
print("- Osea todo esta bien?")
time.sleep(1)

if os.path.exists("carpeta_correcta/dentro_de_carpeta_correcta/text.txt"):
    print("+ Si, mira!!")
    print(', '.join(os.listdir()))
else:
    time.sleep(1)
    print("+ Jummm algo salio mal! T.T\n+ Eliminando todo...")
    print(', '.join(os.listdir()))
    os.remove("text.txt")
    shutil.rmtree("carpeta_correcta")
