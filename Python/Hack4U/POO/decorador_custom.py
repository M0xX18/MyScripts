#!/usr/bin/env python3

def custom(funcion):
    def envoltura():
        print("Antes del saludo")
        funcion()
        print("Despues del saludo")
    return envoltura

@custom
def saludo():
    print("Hola! Soy Andrés")

saludo()
