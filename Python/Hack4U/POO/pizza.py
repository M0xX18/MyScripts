#!/usr/bin/env python3

class Pizza:

    def __init__(self, tamaño, *ingredientes):

        self.tamaño = tamaño
        self.ingredientes = ingredientes

    def describir(self):

        return f"La Pizza tiene un tamaño de {self.tamaño}cms y los ingredientes son: {', '.join(self.ingredientes)}"

pizza_hawaiana = Pizza(20, "Masa", "Piña", "Queso", "Salsa", "Jamón")
print(pizza_hawaiana.describir())
