# O(n^2)
n, m = map(int, input().split())
grafo = {i: {i} for i in range(1, n + 1)}
lista = [1] * n
conexo = 1
 
for i in range(m):
    x, y = map(int, input().split())
    grafo[x].add(y)
    grafo[y].add(x)
 
for i in grafo:
    if lista[i - 1]:
        for j in grafo[i]:
            lista[j - 1] = 0
            if grafo[i] != grafo[j]:
                conexo = 0
 
print('YES') if conexo else print('NO')

