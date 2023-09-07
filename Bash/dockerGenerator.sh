#!/bin/bash

num_contenedores=4

imagen="ubuntu"

codigo_python=$(cat <<EOF

import socket

def recibir_numero(ip, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", puerto))
    s.listen(1)
    conn, addr = s.accept()
    numero = conn.recv(1024).decode()
    conn.close()
    return int(numero)

def enviar_numero(ip_destino, puerto_destino, numero):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_destino, puerto_destino))
    s.send(str(numero).encode())
    s.close()

# Configuración para el contenedor .2
if __name__ == "__main__":
    ip_3 = "172.17.0.3"
    ip_4 = "172.17.0.4"
    ip_5 = "172.17.0.5"

    # Contenedor .2 recibe el número del contenedor .3
    numero_3 = recibir_numero(ip_3, 12345)
    print("Número recibido del contenedor .3:", numero_3)

    # Espera antes de enviar el número al contenedor .3
    input("Presione Enter para continuar...")

    # Contenedor .2 envía el número al contenedor .3
    enviar_numero(ip_3, 12345, numero_3)

    # Contenedor .2 recibe el número del contenedor .4
    numero_4 = recibir_numero(ip_4, 12346)
    print("Número recibido del contenedor .4:", numero_4)

    # Espera antes de enviar el número al contenedor .4
    input("Presione Enter para continuar...")

    # Contenedor .2 envía el número al contenedor .4
    enviar_numero(ip_4, 12346, numero_4)

# Configuración para el contenedor .3
if __name__ == "__main__":
    ip_4 = "172.17.0.4"
    ip_5 = "172.17.0.5"

    # Contenedor .3 recibe el número del contenedor .4
    numero_4 = recibir_numero(ip_4, 12346)
    print("Número recibido del contenedor .4:", numero_4)

    # Espera antes de enviar el número al contenedor .4
    input("Presione Enter para continuar...")

    # Contenedor .3 envía el número al contenedor .4
    enviar_numero(ip_4, 12346, numero_4)

# Configuración para el contenedor .4
if __name__ == "__main__":
    ip_5 = "172.17.0.5"

    # Contenedor .4 recibe el número del contenedor .5
    numero_5 = recibir_numero(ip_5, 12347)
    print("Número recibido del contenedor .5:", numero_5)

    # Espera antes de enviar el número al contenedor .3
    input("Presione Enter para continuar...")

    # Contenedor .4 envía el número al contenedor .3
    enviar_numero(ip_3, 12345, numero_5)

# Configuración para el contenedor .5
if __name__ == "__main__":
    # Contenedor .5 envía un número al contenedor .4
    numero_4 = 99  # Puedes definir el número que quieras
    enviar_numero(ip_4, 12346, numero_4)

EOF
)

comando="mkdir /opt/socket && cd /opt/socket && touch socket_code.py && echo '$codigo_python' > socket_code.py && apt update && apt upgrade -y && apt install neovim nano python3 -y"

for ((i=1; i<=$num_contenedores; i++)); do
    docker run -dit --name "M0xX$i" $imagen
    docker exec -it "M0xX$i" bash -c "$comando"
done

