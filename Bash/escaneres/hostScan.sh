#!/bin/bash

function ctrl_c (){
  echo "\n\n /!/... SALIENDO .../!/ \n"
  exit 1
}

#ctrl_c
trap ctrl_c INT

for host in $(seq 1 254); do
  timeout 1 bash -c "ping -c 1 192.168.0.$host &>/dev/null" && echo "/+/... EL HOST 192.168.0.$host - ESTA ACTIVO .../+/" &
done;wait
