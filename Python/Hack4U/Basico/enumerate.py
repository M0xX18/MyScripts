#!/usr/bin/env python3

nombres = ["Andres", "Paula", "Santiago", "Carlos", "Felipe"]

enum = list(enumerate(nombres))

print (type(enum))
print (list(enumerate(nombres)))
print (list(enumerate(nombres))[2])

for i, nombre in enumerate(nombres):
    print (f"Persona #{i+1} con nombre: {nombre}")
