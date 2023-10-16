# O(q)

n, q = map(int, input().split())
ubicaciones = list(map(int, input().split()))

resultados = []

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        compania = query[1]
        nuevaUbicacion = query[2]
        ubicaciones[compania - 1] = nuevaUbicacion
    elif query[0] == 2:
        i = query[1] - 1
        j = query[2] - 1
        distancia = abs(ubicaciones[i] - ubicaciones[j])
        resultados.append(distancia)

for resultado in resultados:
    print(resultado)

