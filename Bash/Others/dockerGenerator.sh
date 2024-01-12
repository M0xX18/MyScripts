#!/bin/bash
 
num_contenedores=5
imagen="ubuntu"
directorio="/opt/rcp"
comandoCliente="mkdir -p $directorio && cd $directorio && apt update && apt upgrade -y && apt install neovim nano python3 -y && touch cliente.py ordenarServidor.py ordenarCliente.py recibirIps.py"
comandoServer="mkdir -p $directorio && cd $directorio && apt update && apt upgrade -y && apt install neovim nano python3 -y && touch server.py clienteIps.py"
 
for ((i=1; i<=$num_contenedores; i++)); do
    docker run -dit --name "M0xX$i" $imagen
    if [ "$i" -eq 1 ]; then
        docker exec -i "M0xX$i" bash -c "$comandoServer"
    else
        docker exec -i "M0xX$i" bash -c "$comandoCliente"
    fi
done
