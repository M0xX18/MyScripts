#!/bin/bash

calculate_hash() {
  echo -n "$1" | sha256sum | awk '{print $1}'
}

output_file="blockchain.txt"

if [ -e "$output_file" ]; then
  rm "$output_file"
fi

blockchain=("Bloque Génesis")
previous_hash="0"
nonce=0

while true; do
  read -p "Ingrese los datos para almacenar en un bloque: " data

  if [ -z "$data" ]; then
    break
  fi

  current_block="{\"block\": ${#blockchain[@]}, \"data\": \"$data\", \"previous_hash\": \"$previous_hash\", \"nonce\": $nonce}"
  current_hash=$(calculate_hash "$current_block")

  while [[ ! $current_hash =~ ^0000 ]]; do
    nonce=$((nonce + 1))
    current_block="{\"block\": ${#blockchain[@]}, \"data\": \"$data\", \"previous_hash\": \"$previous_hash\", \"nonce\": $nonce}"
    current_hash=$(calculate_hash "$current_block")
  done

  block="Bloque #${#blockchain[@]}\nDatos: \"$data\"\nHash Anterior: \"$previous_hash\"\nNonce: $nonce\nHash Actual: \"$current_hash\"\n"
  blockchain+=("$block")

  echo "Bloque ${#blockchain[@]} creado."
  echo -e "$block" >> "$output_file"
  
  previous_hash="$current_hash"
  nonce=0
done

echo -e "Contenido guardado en: '$output_file':\n"
