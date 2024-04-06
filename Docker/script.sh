#!/bin/bash

num_contenedores=6
imagen="ubuntu"
directorio="/opt/rpc"
ruta_servidor="codigoPython/server"
ruta_cliente="codigoPython/cliente"

comandoCliente="mkdir -p $directorio && cd $directorio && apt update && apt upgrade -y && apt install neovim nano python3 -y && cp -r /scripts/cliente/* ."
comandoServer="mkdir -p $directorio && cd $directorio && apt update && apt upgrade -y && apt install neovim nano python3 -y && cp -r /scripts/server/* ."

for ((i=1; i<=$num_contenedores; i++)); do
    docker run -dit --name "M0xX$i" -v $(pwd)/codigoPython:/scripts $imagen
    if [ "$i" -eq 1 ]; then
        docker exec -it "M0xX$i" bash -c "$comandoServer"
    else
        docker exec -it "M0xX$i" bash -c "$comandoCliente"
    fi
done

