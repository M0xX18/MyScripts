#!/usr/bin/env python3

class Carro:
    def __init__(self, marca, modelo, placa):

        self.marca = marca
        self.modelo = modelo
        self.placa = placa

        self.__kilometraje = 0

    def conducir(self, kilometros):

        self.__kilometraje += kilometros

    def mostrar_kilometraje(self):

        return f"El carro marca '{self.marca}' modelo '{self.modelo}' con placas '{self.placa}' tiene un total de {self.__kilometraje} kilometros recorridos."

mi_carro = Carro("Chevrolet", "Spark", "DB97")
mi_carro.conducir(300)
mi_carro.conducir(400)

# print(mi_carro.__kilometraje)

print(mi_carro.mostrar_kilometraje())
