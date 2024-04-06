import xmlrpc.client
import socket
 
# Función para verificar si un servidor está disponible
def verificar_servidor(ip, puerto):
    try:
        # Intentar crear una conexión TCP con el servidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, puerto))
        return True  # La conexión se realizó con éxito
    except (ConnectionRefusedError, socket.timeout):
        return False  # No se pudo conectar al servidor
 
# Leer las IPs de los servidores desde el archivo
with open('Ips.txt', 'r') as ips_file:
    lineas = ips_file.readlines()
 
# Crear una lista de IPs de servidores disponibles
servidores_disponibles = []
 
# Iterar a través de las líneas y extraer las IPs
for linea in lineas:
    partes = linea.strip().split(', ')
    if len(partes) == 2:
        id_servidor, ip_servidor = partes[0].split(': ')[1], partes[1].split(': ')[1]
        if verificar_servidor(ip_servidor, 8000):
            servidores_disponibles.append((id_servidor, ip_servidor))
 
# Verificar si hay servidores disponibles
if not servidores_disponibles:
    print("No hay ningún servidor disponible")
else:
    # Dirección del servidor RPC
    direccion_servidor = f'http://{servidores_disponibles[0][1]}:8000'  # Usar el primer servidor disponible y los demas no los omite
 
    # Crea un cliente RPC
    cliente = xmlrpc.client.ServerProxy(direccion_servidor, allow_none=True)
 
    # Obtener las listas del servidor
    repetidos_entrantes = cliente.obtener_repetidos()
    faltantes_entrantes = cliente.obtener_faltantes()
    grupo_numeros_ordenados_entrantes = cliente.obtener_grupo_numeros_ordenados()
 
    # Imprimir las listas entrantes del servidor
    print("Listas entrantes del servidor:")
    print("repetidos_entrantes:", repetidos_entrantes)
    print("faltantes_entrantes:", faltantes_entrantes)
    print("grupo_numeros_ordenados_entrantes:", grupo_numeros_ordenados_entrantes)
 
    # Leer las listas locales desde el archivo de texto
    with open('datos_cliente.txt', 'r') as archivo:
        contenido = archivo.read()
 
    # Inicializar las listas locales
    repetidos_locales = []
    faltantes_locales = []
    grupo_numeros_ordenados_locales = []
 
    # Dividir el contenido en líneas
    lineas = contenido.strip().split('\n')
 
    # Variables de estado para rastrear qué lista estamos procesando
    lista_actual = None
 
    # Procesar cada línea
    for linea in lineas:
        linea = linea.strip()
        if linea.startswith("Números repetidos:"):
            lista_actual = repetidos_locales
        elif linea.startswith("Números faltantes:"):
            lista_actual = faltantes_locales
        elif linea.startswith("Grupo de números después de eliminar los repetidos (ordenados):"):
            lista_actual = grupo_numeros_ordenados_locales
        else:
            if lista_actual is not None:
                lista_actual.extend(eval(linea))
 
    # Verificar y ajustar las listas locales si son None
    if repetidos_locales is None:
        repetidos_locales = []
    if faltantes_locales is None:
        faltantes_locales = []
    if grupo_numeros_ordenados_locales is None:
        grupo_numeros_ordenados_locales = []
 
    # Imprimir las listas locales
    print("\nListas locales:")
    print("repetidos_locales:", repetidos_locales)
    print("faltantes_locales:", faltantes_locales)
    print("grupo_numeros_ordenados_locales:", grupo_numeros_ordenados_locales)
 
    # Realizar la negociación
    for numero in repetidos_entrantes:
        if numero in faltantes_locales:
            print("Negociando el número:", numero)
            repetidos_entrantes.remove(numero)
            faltantes_locales.remove(numero)
            grupo_numeros_ordenados_locales.append(numero)
            grupo_numeros_ordenados_locales.sort()
 
    # Actualizar las listas locales en el archivo 'datos_cliente.txt'
    with open('datos_cliente.txt', 'w') as archivo:
        archivo.write("Números repetidos:\n")
        archivo.write(str(repetidos_locales) + '\n')
        archivo.write("Números faltantes:\n")
        archivo.write(str(faltantes_locales) + '\n')
        archivo.write("Grupo de números después de eliminar los repetidos (ordenados):\n")
        archivo.write(str(grupo_numeros_ordenados_locales) + '\n')
 
    # Actualizar las listas en el servidor
    if repetidos_entrantes:
        cliente.actualizar_listas(repetidos_entrantes, faltantes_entrantes, grupo_numeros_ordenados_entrantes)
 
    # Imprimir las listas actualizadas en el servidor
    print("\nListas actualizadas en el servidor:")
    print("repetidos_entrantes:", repetidos_entrantes)
    print("faltantes_locales:", faltantes_locales)
    print("grupo_numeros_ordenados_locales:", grupo_numeros_ordenados_locales)
