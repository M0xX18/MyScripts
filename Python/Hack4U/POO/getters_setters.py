#!/usr/bin/env python3

class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if value > 0:
            self._edad = value
        else:
            raise ValueError("La edad no puede ser menor o igual a 0")

yo = Persona("Andrés", 22)

yo.edad = 30
print(yo.edad)

