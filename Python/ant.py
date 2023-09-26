# O()

num = 1
resultados = []

while True:
    n = int(input())
    if n != 0:
        matriz = [[0] * n for i in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1

        while num <= n * n:
            for i in range(left, right + 1):
                matriz[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                matriz[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                matriz[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matriz[i][left] = num
                num += 1
            left += 1

            for fila in matriz:
                print(' '.join(map(str, fila)))

        resultados.append(n)
    else:
        break

for resultado in resultados:
    print(resultado)
