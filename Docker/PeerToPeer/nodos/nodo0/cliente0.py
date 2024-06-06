import requests
import sys

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Ver estado de mis numeros")
    print("2. Ver estado de numeros vecinos")
    print("3. Obtener y sumar numero del nodo1")
    print("4. Obtener y sumar sumatoria actual nodo1")
    print("5. Salir")

def ver_estado_numeros_nodo0():
    try:
        response = requests.get("http://172.18.0.10:5000/ofrecer_numeros_nodo0")
        if response.status_code == 200:
            datos = response.json()
            print(f"Numero del nodo0: {datos['numero_nodo0']}")
            print(f"Sumatoria actual del nodo0: {datos['sumatoria_actual_del_nodo0']}")
        else:
            print("Error al obtener el estado de los numeros del nodo0")
    except Exception as e:
        print(f"Error: {e}")

def ver_estado_numeros_vecinos():
    try:
        response = requests.get("http://172.18.0.10:5000/obtener_nodo1/sumatoria_actual")
        if response.status_code == 200:
            datos = response.json()
            print(f"Sumatoria actual del nodo1: {datos['sumatoria_actual_del_nodo1']}")
        else:
            print("Error al obtener el estado de los numeros del nodo1")
    except Exception as e:
        print(f"Error: {e}")

def obtener_y_sumar_numero():
    try:
        response = requests.get("http://172.18.0.10:5000/obtener_nodo1/sumar_su_numero")
        if response.status_code == 200:
            datos = response.json()
            print(datos["mensaje"])
            print(f"Sumatoria actual del nodo0: {datos['sumatoria_actual_del_nodo0']}")
        else:
            print("Error al obtener y sumar el numero del nodo1")
    except Exception as e:
        print(f"Error: {e}")

def obtener_y_sumar_sumatoria_actual():
    try:
        response = requests.get("http://172.18.0.10:5000/obtener_nodo1/sumatoria_actual")
        if response.status_code == 200:
            datos = response.json()
            sumatoria_actual_del_nodo1 = datos["sumatoria_actual_del_nodo1"]
            response2 = requests.get("http://172.18.0.10:5000/ofrecer_numeros_nodo0")
            if response2.status_code == 200:
                datos2 = response2.json()
                sumatoria_actual_del_nodo0 = datos2["sumatoria_actual_del_nodo0"]
                sumatoria_actual_del_nodo0 += sumatoria_actual_del_nodo1
                print(f"Sumatoria actual del nodo1: {sumatoria_actual_del_nodo1}")
                print(f"Sumatoria actual del nodo0: {sumatoria_actual_del_nodo0}")
            else:
                print("Error al obtener la sumatoria actual del nodo0")
        else:
            print("Error al obtener la sumatoria actual del nodo1")
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
            ver_estado_numeros_nodo0()
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

