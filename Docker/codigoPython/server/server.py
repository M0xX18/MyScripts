import xmlrpc.server
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
        return self.clients
 
    def save_client_ips(self, file_path):
        with open(file_path, "w") as ips_file:
            for client_id, client_ip in self.clients.items():
                ips_file.write(f"ID: {client_id}, IP: {client_ip}\n")
 
# Lista con todos los números del 0 al 10, cada uno repetido 5 veces
todos_numeros = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4 , 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]
 
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
        return "No hay más grupos disponibles"
 
def main():
    server_ip = "172.17.0.2"
    server_port = 8000
 
    # Crea un servidor RPC
    server = xmlrpc.server.SimpleXMLRPCServer((server_ip, server_port), allow_none=True)
    client_indexer = ClientIndexer()
 
    # Registra métodos RPC del servidor original
    server.register_introspection_functions()
    server.register_function(client_indexer.register_client, "register_client")
    server.register_function(client_indexer.get_client_info, "get_client_info")
    server.register_function(generar_proximo_grupo_numeros, 'generar_proximo_grupo_numeros')
 
    print(f"Servidor RPC esperando conexiones en {server_ip}:{server_port}...")
 
    try:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
 
        while True:
            # Guardar las IPs de los clientes en Ips.txt
            client_indexer.save_client_ips("Ips.txt")
            time.sleep(10)
 
    except KeyboardInterrupt:
        print("Servidor RPC detenido.")
 
if __name__ == "__main__":
    main()
