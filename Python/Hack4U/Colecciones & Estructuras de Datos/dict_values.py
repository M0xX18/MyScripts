#!/usr/bin/env python3

info = {"nombre": "Andres", "edad": 22, "hobbies": "Ciberseguridad"}

print("Las claves de la lista son:")

for element in info:
    print(element)

print("\nLos valores de la lista son:")

for value in info.values():
    print(value)

print("\nLas claves y los valores son:")

for key,value in info.items():
    print(f"La clave {key} tiene el valor {value}")
