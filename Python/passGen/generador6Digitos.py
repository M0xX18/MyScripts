import itertools

# Dígitos permitidos
digitos = '0123456789'

# Longitud de las combinaciones
longitud = 5

# Genera todas las combinaciones posibles
combinaciones = [''.join(p) for p in itertools.product(digitos, repeat=longitud)]

# Guarda las combinaciones en un archivo de texto
with open('combinaciones_5_digitos.txt', 'w') as archivo:
    for combinacion in combinaciones:
        archivo.write(combinacion + '\n')

print(f'Se generaron {len(combinaciones)} combinaciones de 5 dígitos y se guardaron en "combinaciones_5_digitos.txt"')

