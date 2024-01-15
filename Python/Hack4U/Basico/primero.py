#!/usr/bin/python3

my_ports = []

continuar = 1

while (continuar == 1):
    port = int(input("Digite el puerto a agregar a la lista: "))
    if (port != 0):
        my_ports.append(port)
    else:
        continuar -= 1

print(my_ports)
