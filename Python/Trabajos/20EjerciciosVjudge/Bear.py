# O(log(b/a))
a, b = map(int, input().split())
contador = 0
while a <= b:
    a *= 3 
    b *= 2
    contador += 1
print(contador)
