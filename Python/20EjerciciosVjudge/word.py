# O(n) -> n = tamaño de palabra (letra in palabra)
palabra = input()

mayusculas = 0
minusculas = 0

for letra in palabra: 
    if letra.isupper():
        mayusculas += 1
    else:
        minusculas += 1
if mayusculas > minusculas:
    palabra = palabra.upper()
else:
    palabra = palabra.lower()

print(palabra)
