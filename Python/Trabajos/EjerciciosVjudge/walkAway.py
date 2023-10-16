# O(t*n)

t = int(input())

def fun(x, y, d):
    e = (y - x) % d == 0
    return (y - x) // d + 1 - e

for _ in range(t):
    inicio = 0
    n, m, d = map(int, input().split())
    s = list(map(int, input().split()))
    if s[0] != 1:
        inicio = 1
        s.insert(0,1)
    s.append(n + 1)
    n = len(s)
    resultado = 0

    for i in range(1, n):
        resultado += fun(s[i - 1], s[i], d)

    resultado2 = resultado
    nuevo_resultado = resultado

    for i in range (1, n - 1):
        diff = fun(s[i - 1], s[i + 1], d) - fun(s[i - 1], s[i], d) - fun(s[i], s[i + 1], d)
        nuevo_resultado = resultado2 + diff
        resultado = min(resultado, nuevo_resultado)
    contador = 0

    for i in range (1, n - 1):
        diff = fun(s[i - 1], s[i + 1], d) - fun(s[i - 1], s[i], d) - fun(s[i], s[i + 1], d)
        nuevo_resultado = resultado2 + diff
        if nuevo_resultado == resultado:
            contador += 1
    if resultado == resultado2 and inicio == 0:
        contador += 1

    print(resultado, contador)        
