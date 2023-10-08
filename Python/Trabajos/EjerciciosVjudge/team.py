# O(veces)

import sys

def team():
    veces = int(input())

    if 1 <= veces <= 1000:
        respuestas = 0

        for i in range(veces):
            valores = input().split()
            
            if len(valores) == 3 and all(valor in ("0", "1") for valor in valores):
                petya, vasya, tonya = map(int, valores) 
                
                total = petya + vasya + tonya
                
                if total >= 2:
                    respuestas += 1
            else:
                sys.exit() 
        
        print(respuestas) 

if __name__ == "__main__":
    team()

