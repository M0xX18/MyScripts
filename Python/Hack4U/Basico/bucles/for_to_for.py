#!/usr/bin/env python3

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9,0]]
num_list = []
print(listas)

for lista in listas:
    for numeros in lista:
        num_list.append(numeros)

print(num_list)
