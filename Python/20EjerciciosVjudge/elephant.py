# O(coordenada/5)

coordenada = int(input())
pasos = 0

while coordenada > 5:
    pasos += 1
    coordenada -= 5
if coordenada <= 5:
    pasos += 1 
print(pasos)
