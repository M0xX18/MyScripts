#!/usr/bin/env python3

class Calculadora:

    @staticmethod
    def suma(num1,num2):
        return num1 + num2

    @staticmethod
    def resta(num1,num2):
        return num1 - num2
    
    @staticmethod
    def multiplicar(num1,num2):
        return num1 * num2
    
    @staticmethod
    def dividir(num1,num2):
        return num1 // num2 if num2 != 0 else "ERROR: No puedes dividir entre 0"

print(Calculadora.suma(10,8))
print(Calculadora.resta(12,5))
print(Calculadora.multiplicar(4,8))
print(Calculadora.dividir(200,22))
print(Calculadora.dividir(10,0))
