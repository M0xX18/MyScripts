import requests
import sys

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Ver estado de mis numeros")
    print("2. Ver estado de numeros vecinos")
    print("3. Obtener y sumar numero del nodo5")
    print("4. Obtener y sumar sumatoria actual nodo5")
    print("5. Obtener y sumar numero del nodo4")
    print("6. Obtener y sumar sumatoria actual nodo4")
    print("7. Obtener y sumar numero del nodo7")
    print("8. Obtener y sumar sumatoria actual nodo7")
    print("9. Salir")

def ver_estado_numeros_nodo6():
    try:
        response = requests.get("http://172.18.0.16:5006/ofrecer_numeros_nodo6")
        if response.status_code == 200:
            datos = response.json()
            print(f"Numero del nodo6: {datos['numero_nodo6']}")
            print(f"Sumatoria actual del nodo6: {datos['sumatoria_actual_del_nodo6']}")
        else:
            print("Error al obtener el estado de los numeros del nodo6")
    except Exception as e:
        print(f"Error: {e}")

def ver_estado_numeros_vecinos():
    nodos_vecinos = ["nodo5", "nodo4", "nodo7"]
    for nodo in nodos_vecinos:
        try:
            response = requests.get(f"http://172.18.0.16:5006/obtener_nodo{nodo[-1]}/sumatoria_actual")
            if response.status_code == 200:
                datos = response.json()
                print(f"Sumatoria actual del {nodo}: {datos[f'sumatoria_actual_del_{nodo}']}")
            else:
                print(f"Error al obtener el estado de los numeros del {nodo}")
        except Exception as e:
            print(f"Error: {e}")

def obtener_y_sumar_numero(nodo):
    try:
        response = requests.get(f"http://172.18.0.16:5006/obtener_nodo{nodo[-1]}/sumar_su_numero")
        if response.status_code == 200:
            datos = response.json()
            print(datos["mensaje"])
            print(f"Sumatoria actual del nodo6: {datos['sumatoria_actual_del_nodo6']}")
        else:
            print(f"Error al obtener y sumar el numero del {nodo}")
    except Exception as e:
        print(f"Error: {e}")

def obtener_y_sumar_sumatoria_actual(nodo):
    try:
        response = requests.get(f"http://172.18.0.16:5006/obtener_nodo{nodo[-1]}/sumatoria_actual")
        if response.status_code == 200:
            datos = response.json()
            print(f"Sumatoria actual del {nodo}: {datos[f'sumatoria_actual_del_{nodo}']}")
            print(f"Sumatoria actual del nodo6: {datos['sumatoria_actual_del_nodo6']}")
        else:
            print(f"Error al obtener la sumatoria actual del {nodo}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Por favor, ingrese un numero valido.")
            continue

        if opcion == 1:
            ver_estado_numeros_nodo6()
        elif opcion == 2:
            ver_estado_numeros_vecinos()
        elif opcion == 3:
            obtener_y_sumar_numero("nodo5")
        elif opcion == 4:
            obtener_y_sumar_sumatoria_actual("nodo5")
        elif opcion == 5:
            obtener_y_sumar_numero("nodo4")
        elif opcion == 6:
            obtener_y_sumar_sumatoria_actual("nodo4")
        elif opcion == 7:
            obtener_y_sumar_numero("nodo7")
        elif opcion == 8:
            obtener_y_sumar_sumatoria_actual("nodo7")
        elif opcion == 9:
            print("Saliendo del programa.")
            sys.exit(0)
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 9.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVolviendo al menu principal...")

