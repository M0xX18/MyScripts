#!/usr/bin/env python3

my_set = {1,2,3,4,5,6,7,8}

my_set.remove(2) # Solo elimina si existe si no error TypeKey

my_set.discard(7) # Elimina si existe si no, no hace nada, no entra a error, termina exitosamente (0)

print(my_set)
