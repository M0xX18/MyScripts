#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre):

        self.nombre = nombre

    def hablar():

        raise NotImplementedError("Esta accion no se puede hacer sin especificar un animal!")

class Perro(Animal):

    def hablar(self):

        return "Guau!"

class Gato(Animal):

    def hablar(self):
G
        return "Miau!"

def hacer_hablar(objeto):

    print(f"{objeto.nombre} dice {objeto.hablar()}")

gato = Gato("Firulais")
perro = Perro("Maylo")

hacer_hablar(gato)
hacer_hablar(perro)
