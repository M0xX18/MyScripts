#!/bin/bash

function ctrl_c (){
  echo -e "\n\n /!/... SALIENDO .../!/ \n"
  exit 1
}

#ctrl_c
trap ctrl_c INT

function checkPort(){
  (exec 3<> /dev/tcp/$1/$2) 2>/dev/null

  if [ $? -eq 0 ]; then
    echo -e "Host $1 Port $2 OPEN!"
  fi

  exec 3<&-
  exec 3>&-
}

declare -a ports=( $(seq 1 65536) )
if [ $1 ]; then 
  for port in ${ports[@]}; do  
    checkPort $1 $port &
  done
else
  echo -e "\n Se esta usando $0"
fi
