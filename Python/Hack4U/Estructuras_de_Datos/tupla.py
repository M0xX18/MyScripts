#!/usr/bin/env python3

mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9 , 10)

pares = tuple(i for i in mi_tupla if i % 2 == 0)

impares = tuple(i for i in mi_tupla if i % 2 == 1)

print(f"Los numeros pares son: {pares}")
print(f"Los numeros impares son: {impares}")
