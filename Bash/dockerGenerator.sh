#!/bin/bash

num_contenedores=5

imagen="ubuntu"

comando="mkdir /opt/rcp && cd /opt/rcp && apt update && apt upgrade -y && apt install neovim nano python3 -y && touch cliente.py ordenar.py recibirIps.py"

server="import xmlrpc.server
import threading
import time
import random
import socket

class ClientIndexer:
    def __init__(self):
        self.clients = {}
        self.next_id = 1

    def register_client(self, client_ip):
        client_id = str(self.next_id)
        self.clients[client_id] = client_ip
        self.next_id += 1
        return client_id

    def get_client_info(self):
        return self.clients  # Devuelve todo el diccionario de clientes

# Lista con todos los números del 0 al 10, cada uno repetido 4 veces
todos_numeros = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]

# Mezclar la lista para desordenar los números
random.shuffle(todos_numeros)

# Dividir la lista en 4 grupos
grupos = [todos_numeros[i:i + 11] for i in range(0, len(todos_numeros), 11)]

# Variable para llevar un registro del índice del próximo grupo a enviar globalmente
indice_proximo_grupo = 0

# Función para generar el próximo grupo de 11 números desordenados del 0 al 10
def generar_proximo_grupo_numeros():
    global grupos, indice_proximo_grupo

    if indice_proximo_grupo < len(grupos):
        grupo = grupos[indice_proximo_grupo]
        indice_proximo_grupo += 1
        return grupo
    else:
        return \"No hay más grupos disponibles\"

def main():
    # Cambiar la dirección IP del servidor
    server_ip = \"172.17.0.2\"  # Nueva IP del servidor RPC
    server_port = 8000  # Puerto del servidor RPC

    # Crea un servidor RPC
    server = xmlrpc.server.SimpleXMLRPCServer((server_ip, server_port), allow_none=True)
    client_indexer = ClientIndexer()

    # Registra métodos RPC del servidor original
    server.register_introspection_functions()
    server.register_function(client_indexer.register_client, \"register_client\")
    server.register_function(client_indexer.get_client_info, \"get_client_info\")
    server.register_function(generar_proximo_grupo_numeros, 'generar_proximo_grupo_numeros')

    print(f\"Servidor RPC esperando conexiones en {server_ip}:{server_port}...\")

    try:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        while True:
            time.sleep(10)  # Espera durante un tiempo (puedes ajustar este valor)

    except KeyboardInterrupt:
        print(\"Servidor RPC detenido.\")

if __name__ == \"__main__\":
    main()
"

cliente="import xmlrpc.client
import socket

def main_cliente():
    server_ip = \"172.17.0.2\"  # IP del servidor RPC
    server_port = 8000  # Puerto del servidor RPC

    server_url = f\"http://{server_ip}:{server_port}\"
    proxy = xmlrpc.client.ServerProxy(server_url)

    # Obtener la IP del cliente
    client_ip = socket.gethostbyname(socket.gethostname())

    # Registrar al cliente en el servidor y obtener su ID 
    client_id = proxy.register_client(client_ip)

    print(\"---------------------------------------------\")
    
    print(f\"Conectado al servidor RPC en {server_url}\")
    print(f\"IP del cliente: {client_ip}\")
    print(f\"ID del cliente: {client_id}\")

    # Obtener la información de todos los clientes registrados
    client_info = proxy.get_client_info()
    
    print(\"---------------------------------------------\")

    print(\"Clientes registrados:\")
    for client_id, client_ip in client_info.items():
        print(f\"ID {client_id}: {client_ip}\")

    print(\"---------------------------------------------\")
    
    # Solicitar el próximo grupo de números al servidor
    grupo_numeros = proxy.generar_proximo_grupo_numeros()

    if grupo_numeros == \"No hay más grupos disponibles\":
        print(\"No hay más grupos disponibles\")
    else:
        print(\"Grupo de números recibido:\", grupo_numeros)

        print(\"---------------------------------------------\")
        
        # Crear una lista para rastrear los números repetidos
        repetidos = []

        # Eliminar los números repetidos de 'grupo_numeros'
        grupo_numeros_sin_repetir = []
        for numero in grupo_numeros:
            if numero in grupo_numeros_sin_repetir:
                repetidos.append(numero)
            else:
                grupo_numeros_sin_repetir.append(numero)

        # Ordenar la lista 'grupo_numeros_sin_repetir'
        grupo_numeros_sin_repetir.sort()

        # Crear una lista de números desde un rango específico
        rango_numeros = list(range(0, 11))  # Cambia el rango según tus necesidades (de 0 a 10 inclusive)

        # Identificar los números que hacen falta en 'grupo_numeros_sin_repetir'
        numeros_faltantes = list(set(rango_numeros) - set(grupo_numeros_sin_repetir))

        # Guardar las listas en un archivo de texto
        with open('datos_cliente.txt', 'w') as archivo_txt:
            archivo_txt.write(\"Grupo de números:'/n\")
            archivo_txt.write(str(grupo_numeros) + '/n')

            archivo_txt.write(\"Números repetidos:/n\")
            archivo_txt.write(str(repetidos) + '/n')

            archivo_txt.write(\"Grupo de números después de eliminar los repetidos (ordenados):/n\")
            archivo_txt.write(str(grupo_numeros_sin_repetir) + '/n')

            archivo_txt.write(\"Números faltantes:/n\")
            archivo_txt.write(str(numeros_faltantes) + '/n')

if __name__ == \"__main__\":
    main_cliente()"
    
ordenar="import xmlrpc.client
import socket
import json

# Función para procesar una IP y actualizar los datos
def procesar_ip(ip, datos):
    try:
        # Crear un cliente RPC para la IP
        server_url = f\"http://{ip}:8000\"  # Ajusta el puerto según tu configuración
        proxy = xmlrpc.client.ServerProxy(server_url)

        # Llama a un método RPC para obtener datos actualizados de la IP
        datos_actualizados = proxy.obtener_datos()

        # Realiza las actualizaciones en las listas locales según los datos recibidos
        # Por ejemplo, puedes comparar y fusionar las listas según tus necesidades
        datos[\"grupo_numeros\"] = datos_actualizados[\"grupo_numeros\"]
        datos[\"numeros_repetidos\"] = datos_actualizados[\"numeros_repetidos\"]
        datos[\"grupo_numeros_sin_repetir\"] = datos_actualizados[\"grupo_numeros_sin_repetir\"]
        datos[\"numeros_faltantes\"] = datos_actualizados[\"numeros_faltantes\"]

        print(f\"Datos actualizados de la IP {ip}\")
    except Exception as e:
        print(f\"Error al conectar con {ip}: {e}\")

# Función para cargar datos desde un archivo de texto
def cargar_datos_desde_archivo():
    datos = {
        \"grupo_numeros\": [],
        \"numeros_repetidos\": [],
        \"grupo_numeros_sin_repetir\": [],
        \"numeros_faltantes\": []
    }

    with open(\"datos_cliente.txt\", \"r\") as archivo_txt:
        linea = archivo_txt.readline().strip()
        while linea:
            if linea == \"Grupo de números:\":
                lista = eval(archivo_txt.readline().strip())
                datos[\"grupo_numeros\"] = lista
            elif linea == \"Números repetidos:\":
                lista = eval(archivo_txt.readline().strip())
                datos[\"numeros_repetidos\"] = lista
            elif linea == \"Grupo de números después de eliminar los repetidos (ordenados):\":
                lista = eval(archivo_txt.readline().strip())
                datos[\"grupo_numeros_sin_repetir\"] = lista
            elif linea == \"Números faltantes:\":
                lista = eval(archivo_txt.readline().strip())
                datos[\"numeros_faltantes\"] = lista
            linea = archivo_txt.readline().strip()

    return datos

# Función para imprimir las listas
def imprimir_listas(datos):
    print(\"Grupo de números:\", datos[\"grupo_numeros\"])
    print(\"Números repetidos:\", datos[\"numeros_repetidos\"])
    print(\"Grupo de números después de eliminar los repetidos (ordenados):\", datos[\"grupo_numeros_sin_repetir\"])
    print(\"Números faltantes:\", datos[\"numeros_faltantes\"])

# Función para enviar datos a otro cliente
def enviar_datos(ip_destino, puerto_destino, datos):
    try:
        # Crea un socket y conecta con el cliente destino
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_destino, puerto_destino))
            # Convierte los datos a JSON y envía
            datos_json = json.dumps(datos)
            s.sendall(datos_json.encode('utf-8'))
            print(f\"Datos enviados a {ip_destino}:{puerto_destino}\")
    except Exception as e:
        print(f\"Error al enviar datos a {ip_destino}:{puerto_destino}: {e}\")

# Función para recibir datos de otro cliente
def recibir_datos(puerto):
    try:
        # Crea un socket y escucha las conexiones entrantes
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', puerto))
            s.listen()
            conn, addr = s.accept()
            with conn:
                datos_json = conn.recv(1024).decode('utf-8')
                datos = json.loads(datos_json)
                print(f\"Datos recibidos de {addr[0]}:{addr[1]}\")
                return datos
    except Exception as e:
        print(f\"Error al recibir datos: {e}\")
        return None

def main():
    datos = cargar_datos_desde_archivo()
    ips_list = []

    # Leer el archivo de texto \"ips.txt\" y agregar las IPs a la lista
    with open(\"ips.txt\", \"r\") as file:
        for line in file:
            ips_list.append(line.strip())  # Elimina el salto de línea

    # Iterar y procesarcada IP en la lista
    for ip in ips_list:
        procesar_ip(ip, datos)

    # Imprimir las listas
    imprimir_listas(datos)

    # Operaciones en las listas

    # Ejemplo: Enviar datos a otro cliente
    ip_destino = '192.168.1.100'  # IP del cliente destino
    puerto_destino = 12345  # Puerto del cliente destino
    enviar_datos(ip_destino, puerto_destino, datos)

    # Ejemplo: Recibir datos de otro cliente
    puerto_cliente2 = 54321  # Puerto de este cliente para recibir datos
    datos_recibidos = recibir_datos(puerto_cliente2)

    # Realiza las modificaciones necesarias en las listas locales según los datos recibidos
    # Por ejemplo, puedes comparar y fusionar las listas según tus necesidades

    # Imprimir las listas actualizadas
    print(\"Listas actualizadas:\")
    imprimir_listas(datos)

if __name__ == \"__main__\":
    main()"
    
recibirIps="# Código de recibirIps.py
import xmlrpc.client

def main():
    server_ip = \"172.17.0.2\"  # IP del servidor RPC
    server_port = 8000  # Puerto del servidor RPC

    server_url = f\"http://{server_ip}:{server_port}\"
    proxy = xmlrpc.client.ServerProxy(server_url)

    try:
        # Solicitar la información de clientes al servidor
        client_info = proxy.get_client_info()
        if client_info:
            # Obtener la lista de direcciones IP del diccionario de clientes
            ips_list = list(client_info.values())

            # Guardar la lista de IPs en un archivo de texto
            with open(\"ips.txt\", \"w\") as ips_file:
                for ip in ips_list:
                    ips_file.write(ip + \"\\n\")
                print(\"Lista de IPs guardada en 'ips.txt'\")
        else:
            print(\"No se encontraron clientes registrados.\")
    except Exception as e:
        print(f\"No se pudo obtener la información de clientes: {e}\")

if __name__ == \"__main__\":
    main()"

for ((i=1; i<=$num_contenedores; i++)); do
    docker run -dit --name "M0xX$i" $imagen
    docker exec -it "M0xX$i" bash -c "$comando"
    echo -e "$cliente" | docker exec -i "M0xX$i" bash -c "cat > /opt/rcp/cliente.py"
    echo -e "$ordenar" | docker exec -i "M0xX$i" bash -c "cat > /opt/rcp/ordenar.py"
    echo -e "$recibirIps" | docker exec -i "M0xX$i" bash -c "cat > /opt/rcp/recibirIps.py"
    
    if [ "$i" -eq 1 ]; then
        echo -e "$server" | docker exec -i "M0xX$i" bash -c "cat > /opt/rcp/server.py"
        comandoM0xX1="cd /opt/rcp && rm cliente.py ordenar.py recibirIps.py"
      docker exec -it "M0xX$i" bash -c "$comandoM0xX1"
    fi
done
