# O(t*mex)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lista = list(map(int, input().split()))
    s = set(lista)
    max_lista = max(lista)
    mex = 0

    if max_lista == n - 1:
        print(n + k)
        continue

    for i in range(int(1e9)):
        if i not in s:
            mex = i
            break

    unicos = (max_lista + mex + 1) // 2
    add = (k > 0) * (1 - int(unicos in s))
    print(len(s) + add)

