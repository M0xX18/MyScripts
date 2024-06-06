import requests
import sys

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Ver estado de mis numeros")
    print("2. Ver estado de numeros vecinos")
    print("3. Obtener y sumar numero del nodo6")
    print("4. Obtener y sumar sumatoria actual nodo6")
    print("5. Salir")

def ver_estado_numeros_nodo7():
    try:
        response = requests.get("http://172.18.0.17:5007/ofrecer_numeros_nodo7")
        if response.status_code == 200:
            datos = response.json()
            print(f"Numero del nodo7: {datos['numero_nodo7']}")
            print(f"Sumatoria actual del nodo7: {datos['sumatoria_actual_del_nodo7']}")
        else:
            print("Error al obtener el estado de los numeros del nodo7")
    except Exception as e:
        print(f"Error: {e}")

def ver_estado_numeros_vecinos():
    nodos_vecinos = ["nodo6"]
    for nodo in nodos_vecinos:
        try:
            response = requests.get(f"http://172.18.0.17:5007/obtener_nodo{nodo[-1]}/sumatoria_actual")
            if response.status_code == 200:
                datos = response.json()
                print(f"Sumatoria actual del {nodo}: {datos['sumatoria_actual_del_nodo6']}")
            else:
                print(f"Error al obtener el estado de los numeros del {nodo}")
        except Exception as e:
            print(f"Error: {e}")

def obtener_y_sumar_numero():
    try:
        response = requests.get("http://172.18.0.17:5007/obtener_nodo6/sumar_su_numero")
        if response.status_code == 200:
            datos = response.json()
            print(datos["mensaje"])
            print(f"Sumatoria actual del nodo7: {datos['sumatoria_actual_del_nodo7']}")
        else:
            print("Error al obtener y sumar el numero del nodo6")
    except Exception as e:
        print(f"Error: {e}")

def obtener_y_sumar_sumatoria_actual():
    try:
        response = requests.get("http://172.18.0.17:5007/obtener_nodo6/sumatoria_actual")
        if response.status_code == 200:
            datos = response.json()
            print(f"Sumatoria actual del nodo6: {datos['sumatoria_actual_del_nodo6']}")
            print(f"Sumatoria actual del nodo7: {datos['sumatoria_actual_del_nodo7']}")
        else:
            print("Error al obtener la sumatoria actual del nodo6")
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
            ver_estado_numeros_nodo7()
        elif opcion == 2:
            ver_estado_numeros_vecinos()
        elif opcion == 3:
            obtener_y_sumar_numero()
        elif opcion == 4:
            obtener_y_sumar_sumatoria_actual()
        elif opcion == 5:
            print("Saliendo del programa.")
            sys.exit(0)
        else:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nVolviendo al menu principal...")

