import xmlrpc.client
import socket
 
def main_cliente():
    server_ip = "172.17.0.2"
    server_port = 8000
 
    server_url = f"http://{server_ip}:{server_port}"
    proxy = xmlrpc.client.ServerProxy(server_url)
 
    # Obtener la IP del cliente
    client_ip = socket.gethostbyname(socket.gethostname())
 
    # Registrar al cliente en el servidor y obtener su ID
    client_id = proxy.register_client(client_ip)
 
    print("---------------------------------------------")
 
    print(f"Conectado al servidor RPC en {server_url}")
    print(f"IP del cliente: {client_ip}")
    print(f"ID del cliente: {client_id}")
 
    # Obtener la información de todos los clientes registrados
    client_info = proxy.get_client_info()
 
    print("---------------------------------------------")
 
    print("Clientes registrados:")
    for client_id, client_ip in client_info.items():
        print(f"ID {client_id}: {client_ip}")
 
    print("---------------------------------------------")
 
    # Solicitar el próximo grupo de números al servidor
    grupo_numeros = proxy.generar_proximo_grupo_numeros()
 
    if grupo_numeros == "No hay más grupos disponibles":
        print("No hay más grupos disponibles")
    else:
        print("Grupo de números recibido:", grupo_numeros)
 
        print("---------------------------------------------")
 
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
 
        # Crear una lista de números desde un rango de numero 0-10 (11 numeros)
        rango_numeros = list(range(0, 11))
 
        # Identificar los números que hacen falta en 'grupo_numeros_sin_repetir'
        numeros_faltantes = list(set(rango_numeros) - set(grupo_numeros_sin_repetir))
 
        # Guardar las listas en un archivo txt
        with open('datos_cliente.txt', 'w') as archivo_txt:
            archivo_txt.write("Números repetidos:\n")
            archivo_txt.write(str(repetidos) + "\n")
 
            archivo_txt.write("Números faltantes:\n")
            archivo_txt.write(str(numeros_faltantes) + "\n")
 
            archivo_txt.write("Grupo de números después de eliminar los repetidos (ordenados):\n")
            archivo_txt.write(str(grupo_numeros_sin_repetir) + "\n")
 
if __name__ == "__main__":
    main_cliente()
