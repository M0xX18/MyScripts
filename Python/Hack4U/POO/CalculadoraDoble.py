#!/usr/bin/env python3

class Calculadora:

    def __init__(self, numero):
        self.numero = numero

    def suma(self, otro_numero):
        return self.numero + otro_numero

    def doble_suma(self, num1, num2):
        return self.suma(num1) + self.suma(num2)


calc = Calculadora(5)
calc.suma(8)
print(calc.doble_suma(2,7))
