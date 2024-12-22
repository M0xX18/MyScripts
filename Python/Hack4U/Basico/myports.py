#!/usr/bin/env python3

contador = 0

my_ports= [22,80,8080]

my_ports.append(44)

my_ports.extend([445,446])

my_ports = sorted(my_ports)

for port in my_ports:
    print(f"El puerto #{contador} es: " + str(my_ports[contador]))
    contador += 1

print(my_ports[0])
