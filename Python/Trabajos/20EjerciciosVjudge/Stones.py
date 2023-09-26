# O(n)
n = int(input())
piedras = list(input())
contador = 0
if len(piedras) == n:
    for i in range (n - 1):
        if piedras[i] == piedras[i+1]:
            contador += 1
print(contador)
