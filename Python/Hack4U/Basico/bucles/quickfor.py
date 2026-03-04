#!/usr/bin/env python3

listas = [[1,2,3], [4,5,6], [7,8,9,0]]
num_list = []

result = [(numero, lista) for lista in listas for numero in lista]

print(result)
