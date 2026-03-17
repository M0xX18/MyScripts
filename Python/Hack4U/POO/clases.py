#!/usr/bin/env python3

class Persona:
    
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludo(self):

        print(f"Hola mi nombre es {self.nombre} tengo {self.edad} años.")

andres = Persona("Andres", 22)

andres.saludo()
