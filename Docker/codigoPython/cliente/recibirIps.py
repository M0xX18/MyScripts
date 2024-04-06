import xmlrpc.server
 
# Definir una función que recibe el archivo en el servidor RPC
def receive_file(file_content, file_name):
    try:
        with open(file_name, 'w') as f:
            f.write(file_content)
        return f"Archivo recibido correctamente en {file_name}"
    except Exception as e:
        return f"Error al recibir archivo en {file_name}: {str(e)}"
 
# Crear un servidor RPC en la dirección IP y puerto correspondiente
ip_address = "172.17.0.3"
port = 8000
server = xmlrpc.server.SimpleXMLRPCServer((ip_address, port))
server.register_function(receive_file)
 
print(f"Servidor RPC en ejecución en {ip_address}:{port}")
server.serve_forever()
