texto = "Hola, esto, es, un nuevo, texto"

nuevo_texto = texto.split(',')

for i in range(3):
    print(''.join(nuevo_texto[i].split()))

end = nuevo_texto[-1]
print(''.join(end.split()))
