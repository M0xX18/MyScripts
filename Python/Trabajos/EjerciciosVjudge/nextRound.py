#O(notaas)

import sys

def domino():
    n, k = map(int, input().split())

    notas = list(map(int, input().split()))
    
    contador = 0

    if len(notas) != n:
        sys.exit()
    else:
        for nota in notas:
            if k < nota:
                contador += 1

    print(contador)

if __name__ == "__main__":
    domino()

