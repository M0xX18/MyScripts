#!/usr/bin/env python3

class Libro:

    IVA = 0.25
    best_seller_value = 5000

    def __init__(self, titulo, autor, precio):

        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod
    def es_best_seller(total_ventas):

        return total_ventas > Libro.best_seller_value

    @classmethod
    def precio_con_iva(cls, precio):

        return precio + precio * cls.IVA

class LibroDigital(Libro):

    IVA = 0.10

mi_libro = Libro("La moraleja de ser cacorra", "Paula K. Leal", 42000)
mi_libro_digital = LibroDigital("La moraleja de ser cacorra", "Paula K. Leal", 42000)

print(f"El libro titulado '{mi_libro.titulo}' de la famosa autora '{mi_libro.autor}' es best seller? -> {mi_libro.es_best_seller(6000)}")

print(f"El precio con IVA del libro {mi_libro.titulo} es de {Libro.precio_con_iva(mi_libro.precio)}")
print(f"El precio con IVA del libro digital {mi_libro.titulo} es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)}")
