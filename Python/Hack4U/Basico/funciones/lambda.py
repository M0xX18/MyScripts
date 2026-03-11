#!/usr/bin/env python3

from functools import reduce

lista = ['Paula', 3, 'Andres', 6, 'Stefi', 9]

nombres = []

nueva_lista = list(filter(lambda x: isinstance(x, str), lista))

solo_numeros = list(filter(lambda x: isinstance(x, int), lista))

multiplicador = reduce(lambda x, y: x*y, solo_numeros)

nueva_lista = [nombre.lower() for nombre in nueva_lista]

repetidas = reduce(lambda x, y: count(y), nueva_lista[caracter(posicion pues)])

print(nueva_lista)
print(multiplicador)
print(repetidas)
