# O(1)

matriz = []
for i in range(5):
    fila = list(map(int, input().split()))
    matriz.append(fila)

for fila_idx, fila in enumerate(matriz):
    for columna_idx, valor in enumerate(fila):
        if valor != 0:
            fila_faltante = abs(2 - fila_idx)
            columna_faltante = abs(2 - columna_idx)
 
            suma_diferencias = fila_faltante + columna_faltante
            print(suma_diferencias)
