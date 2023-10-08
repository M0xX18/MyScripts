def dividir_sandia(w):
    if w > 2 and w % 2 == 0:
        return "YES"  
    else:
        return "NO"

w = int(input())

resultado = dividir_sandia(w)
print(resultado)

