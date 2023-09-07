def palabrasLargas():
    veces = int(input())
    
    if 1 <= veces <= 100:
        palabrasProcesadas = []

        for i in range(veces):
            palabra = input()
            tamaño = len(palabra)

            if tamaño > 10:
                palabra = palabra[0] + str(tamaño - 2) + palabra[-1]
            palabrasProcesadas.append(palabra)
        
        for palabra in palabrasProcesadas:
            print(palabra)

if __name__ == "__main__":
    palabrasLargas()

