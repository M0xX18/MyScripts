#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre):

        self.nombre = nombre

    def hablar(self):

        raise NotImplementedError("Se deberia implementar este metodo en las subclases!")

class Perro(Animal):
    
    def hablar(self):
        return f"{self.nombre} es un perrito!!"


class Gato(Animal):

    def hablar(self):
        return f"{self.nombre} es un gatico!!"

gato_uno = Gato("Michi")
perro_uno = Perro("Arabella")

print(gato_uno.hablar())
print(perro_uno.hablar())
