import xmlrpc.client
 
# Leer el archivo txt y analizar las IDs e IPs
with open('Ips.txt', 'r') as file:
    lines = file.readlines()
 
for line in lines:
    if 'ID' in line and 'IP' in line:
        parts = line.split(', ')
        id = parts[0].split(':')[1].strip()
        ip = parts[1].split(':')[1].strip()
 
        # Leer el archivo que deseas enviar
        with open('Ips.txt', 'r') as file_to_send:
            file_content = file_to_send.read()
 
        try:
            # Crear un cliente RPC y enviar el archivo a la dirección IP correspondiente
            proxy = xmlrpc.client.ServerProxy(f"http://{ip}:8000/")
            result = proxy.receive_file(file_content, 'Ips.txt')
            print(result)
        except ConnectionRefusedError:
            print(f"No se pudo conectar al servidor RPC en la dirección IP {ip}.")
        except Exception as e:
            print(f"Error al enviar archivo a {ip}: {str(e)}")
