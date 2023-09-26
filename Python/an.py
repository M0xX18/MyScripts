def generar_coordenadas_espiral(n):
    if n < 1:
        return []

    coordenadas = [(0, 0)]
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while len(coordenadas) < n * n:
        for i in range(left, right + 1):
            coordenadas.append((top, i))
        top += 1

        for i in range(top, bottom + 1):
            coordenadas.append((i, right))
        right -= 1

        for i in range(right, left - 1, -1):
            coordenadas.append((bottom, i))
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            coordenadas.append((i, left))
        left += 1

    return coordenadas

def obtener_coordenada(coordenadas, numero):
    if numero < 1 or numero > len(coordenadas):
        return None
    x, y = coordenadas[numero - 1]
    return f"{x} {y}"

def main():
    try:
        n = int(input("Ingrese un número entero para generar las coordenadas en espiral: "))
        if n <= 0:
            print("El número debe ser mayor que cero.")
            return
    except ValueError:
        print("Entrada inválida. Ingrese un número entero positivo.")
        return

    coordenadas = generar_coordenadas_espiral(n)
    while True:
        numero = int(input("Ingrese un número para obtener su coordenada (o 0 para salir): "))
        if numero == 0:
            break
        coordenada = obtener_coordenada(coordenadas, numero)
        if coordenada:
            print(coordenada)
        else:
            print(f"El número {numero} está fuera de rango.")

if __name__ == "__main__":
    main()

