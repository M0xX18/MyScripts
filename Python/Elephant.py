try:
    coordenada = int(input())
except ValueError:
    print("Ingresa un número válido.")

pasos = 0

if coordenada > 5:
    pasos = coordenada // 5
    if coordenada % 5 != 0:
        pasos += 1
else:
    pasos = 1

print(pasos)

