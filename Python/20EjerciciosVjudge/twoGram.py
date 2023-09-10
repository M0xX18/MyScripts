n = int(input())
cadena = input()

def similitudes(sub):
    contador = 0

    for i in range(len(cadena) - 1):
        if cadena[i] == sub[0] and cadena[i + 1] == sub[1]:
            contador += 1

    return contador

totalSimilitudes = 0
resultado = ""

for i in range(len(cadena) - 1):
    sub = cadena[i:i + 2]

    x = similitudes(sub)

    if x > totalSimilitudes:
        totalSimilitudes = x
        resultado = sub

print(resultado)

