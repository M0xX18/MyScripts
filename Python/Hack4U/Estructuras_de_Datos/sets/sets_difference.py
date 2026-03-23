#!/usr/bin/env python3

amigos = {"Andres", "Paula", "Papitas", "Stefi", "Katherine"}

enemigos = {"Andres", "Stefi", "Eduardo"}

mejores_amigos = amigos.difference(enemigos)
mayores_enemigos = enemigos.difference(amigos)

print(mejores_amigos)
print(mayores_enemigos)
