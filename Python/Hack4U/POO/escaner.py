#!/usr/bin/env python3

class Dispositivo:

    def __init__(self, modelo):

        self.modelo = modelo

    def escanear_vulnerabilidades():

        raise NotImplementedError("Para usar esta opcion se deberia especificar dentro de la subclases de este componente")


class Computador(Dispositivo):

    def escanear_vulnerabilidades(self):

        return f"Escaneo de vulnerabilidades detectado para el computador '{self.modelo}'"

class Telefono(Dispositivo):

    def escanear_vulnerabilidades(self):
        
        return f"Escaneo de vulnerabilidades detectado para el telefono '{self.modelo}'"

def escanear(dispositivo):

    print(dispositivo.escanear_vulnerabilidades())

mi_pc = Computador("HP ProBook")
mi_celular = Telefono("Samsung Galaxy S25 Ultra")

escanear(mi_pc)
escanear(mi_celular)
