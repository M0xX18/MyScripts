#!/bin/bash

function ctrl_c (){
  echo -e "\n\n /!/... SALIENDO .../!/ \n"
  exit 1
}

#ctrl_c
trap ctrl_c INT

for port in $(seq 1 65536); do
  (echo '' > /dev/tcp/127.0.0.1/$port) 2>/dev/null && echo "/!/... $port OPEN .../!/"
done
