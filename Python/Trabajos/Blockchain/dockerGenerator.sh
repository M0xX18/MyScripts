#!/bin/bash

num_contenedores=4
imagen="ubuntu"
comandoCliente="cd /opt/ && apt update && apt upgrade -y && apt install neovim python3 pip -y && pip install flask requests"

puerto_base=5000

for ((i=1; i<=$num_contenedores; i++)); do
    puerto_host=$((puerto_base + i - 1))
    docker run -dit --name "M0xX$i" -p $puerto_host:5000 -v /home/m0xx/Utilidades/MyScripts/Python/Trabajos/Blockchain/:/opt/con $imagen
    docker exec -i "M0xX$i" bash -c "$comandoCliente"
done
