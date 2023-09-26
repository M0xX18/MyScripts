# O(1)

k, n, w = map(int, input().split())
precio = (w * (w + 1) // 2) * k
prestado = max(0, precio - n)

print(prestado)
