# O(veces)
veces = int(input())
contador = 0

for i in range(veces):
    contador = contador + 1 if '+' in input() else contador - 1

print(contador)
