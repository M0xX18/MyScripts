import xmlrpc.server
import os
 
# Clase que contiene los métodos para el servidor RPC
class MiServidor:
    def __init__(self, archivo_cliente):
        self.archivo_cliente = archivo_cliente
        self.leer_listas_desde_archivo(self.archivo_cliente)
 
    def leer_listas_desde_archivo(self, archivo_nombre):
        # Inicializar las listas vacías
        self.repetidos = []
        self.faltantes = []
        self.grupo_numeros_ordenados = []
 
        # Leer el contenido del archivo txt y extraer las listas
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
 
        # Dividir el contenido en líneas
        lineas = contenido.strip().split('\n')
 
        # Variables de estado para rastrear qué lista estamos procesando
        lista_actual = None
 
        # Procesar cada línea
        for linea in lineas:
            linea = linea.strip()
            if linea.startswith("Números repetidos:"):
                lista_actual = self.repetidos
            elif linea.startswith("Números faltantes:"):
                lista_actual = self.faltantes
            elif linea.startswith("Grupo de números después de eliminar los repetidos (ordenados):"):
                lista_actual = self.grupo_numeros_ordenados
            else:
                if lista_actual is not None:
                    lista_actual.extend(eval(linea))
 
    def pasar_repetidos(self, lista):
        self.repetidos = lista
 
    def pasar_faltantes(self, lista):
        self.faltantes = lista
 
    def pasar_grupo_numeros_ordenados(self, lista):
        self.grupo_numeros_ordenados = lista
 
    def obtener_repetidos(self):
        return self.repetidos
 
    def obtener_faltantes(self):
        return self.faltantes
 
    def obtener_grupo_numeros_ordenados(self):
        return self.grupo_numeros_ordenados
 
    def actualizar_listas(self, repetidos, faltantes, grupo_numeros_ordenados):
        # Actualizar las listas en el servidor
        self.repetidos = repetidos
        self.faltantes = faltantes
        self.grupo_numeros_ordenados = grupo_numeros_ordenados
 
        # Actualizar el archivo txt con las listas actualizadas
        with open(self.archivo_cliente, 'w') as archivo:
            archivo.write("Números repetidos:\n" + str(repetidos) + "\n")
            archivo.write("Números faltantes:\n" + str(faltantes) + "\n")
            archivo.write("Grupo de números después de eliminar los repetidos (ordenados):\n" + str(grupo_numeros_ordenados) + "\n")
 
if __name__ == "__main__":
    # Nombre del txt con las listas del cliente
    archivo_cliente = 'datos_cliente.txt'
 
    # Inicializar y leer las listas desde el archivo
    servidor = MiServidor(archivo_cliente)
 
    # Configura y inicia el servidor RPC
    servidor_rpc = xmlrpc.server.SimpleXMLRPCServer(('172.17.0.3', 8000), allow_none=True)
    servidor_rpc.register_instance(servidor)
    print("Servidor RPC iniciado en el puerto 8000...")
    servidor_rpc.serve_forever()
