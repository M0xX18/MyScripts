#!/bin/bash

function ctrl_c ()
{
  echo -e "\n\n/!/... SALIENDO .../!/\n\n"
  exit 1
}

#ctrol_c
trap ctrl_c INT

echo -e "\n/?/... Por favor, ingresa el nombre del archivo ubicado en la carpeta actual .../?/\n\n$(ls)\n"
echo "/?/... ¿Que archivo desea elegir? .../?/"
read nombre_archivo

echo "Has ingresado el archivo: $nombre_archivo"

nombre_archivo_descomprimido="$(7z l $nombre_archivo | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"

7z x $nombre_archivo &>/dev/null

while [ $nombre_archivo_descomprimido ]; do
  echo -e "[-] El nuevo archivo descomprimido es $nombre_archivo_descomprimido [-]"
  7z x $nombre_archivo_descomprimido &>/dev/null
  nombre_archivo_descomprimido="$(7z l $nombre_archivo_descomprimido 2>/dev/null | tail -n 3 | head -n 1 | awk 'NF{print $NF}')"
done
