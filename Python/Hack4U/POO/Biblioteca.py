#!/usr/bin/env python3

class Libro:

    def __init__(self, titulo, autor, disponible):

        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

class Usuario:

    def __init__(self, nombre, id_usuario, lista_libros_pretados):

        self.nombre = nombre
        self.id_usuario = id_usuario
        self.lista_libros_prestados = lista_libros_prestados

class Biblioteca:

    def __init__(self, lista_libros, lista_usuarios):

        self.lista_libros = lista_libros
        self.lista_usuarios = lista_usuarios

    def agregar_libro(self):


    def registrar_usuario():


    def prestar_libro():


    def devolver_libro():



