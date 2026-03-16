#!/usr/bin/env python3

juegos = ["Valorant", "Minecraft", "LoL", "Sekiro"]

categoria = {
        "Valorant": "Shooter",
        "Minecraft": "Aventura",
        "LoL": "Moba",
        "Sekiro": "Souls"
}

ventas_y_stock = {
        "Valorant": (2185, 51),
        "Minecraft": (4092, 8),
        "LoL": (10, 500),
        "Sekiro": (1200, 100)
}

clientes = {
        "Valorant": ["Andres", "Papitas", "Lucho"],
        "Minecraft": ["M0xX", "Stefi", "Paula"],
        "LoL": ["Stefi"],
        "Sekiro": ["Andres", "M0xX", "Lucho"]
}

def sumario(juego):
    print(f"La categoria del juego es: {categoria[juego]}")
    print(f"El juego ha vendido {ventas_y_stock[juego][0]} unidades")
    print(f"Actualmente tenemos {ventas_y_stock[juego][1]} unidades")
    print(f"Las personas que han comprado el juego han sido {clientes[juego]}")

def main():
    juego = input((f"Bienvenido! Digita un Videojuego de la lista \n/ {' / '.join(juegos)} / \n"))

    if juego in juegos:
        sumario(juego)
    else:
        while juego not in juegos:
            juego = input(f"Este juego no pertenece a la lista, usted esta bien pendejo digitelo bien.\n")
        sumario(juego)

    ventas_totales = lambda: sum(ventas for ventas, _ in ventas_y_stock.values())

    print(f"Las ventas totales fueron de {ventas_totales()} unidades")

if __name__ == "__main__":
    main()
