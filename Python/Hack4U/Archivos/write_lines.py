#!/usr/bin/env python3

lista = ["Manzana\n", "Pera\n", "Aguacate\n", "Guanabana\n"]

with open("test.txt", "w") as f:
    f.writelines(lista)
