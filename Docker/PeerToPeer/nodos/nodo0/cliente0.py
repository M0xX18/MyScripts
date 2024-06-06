import requests

def mostrar_menu():
    print("\n--- Menú del Cliente Nodo0 ---")
    print("1. Ver estado de mis números")
    print("2. Ver estado de números vecinos")
    print("3. Obtener y sumar número del nodo1")
    print("4. Ver sumatoria actual del nodo1")
    print("5. Salir")

def ver_estado_mis_numeros():
    try:
        response = requests.get("http://localhost:5000/ofrecer_numeros_nodo0")
        if response.status_code == 200:
            print("Estado de mis números:")
            print(response.json())
        else:
            print("Error al obtener el estado de mis números.")
    except Exception as e:
        print(f"Excepción al obtener el estado de mis números: {str(e)}")

def ver_estado_numeros_vecinos():
    try:
        response_nodo1 = requests.get("http://172.18.0.11:5001/ofrecer_numeros_nodo1")
        if response_nodo1.status_code == 200:
            print("Estado de los números del nodo1:")
            print(response_nodo1.json())
        else:
            print("Error al obtener el estado de los números del nodo1.")
    except Exception as e:
        print(f"Excepción al obtener el estado de los números del nodo1: {str(e)}")

def obtener_y_sumar_numero_nodo1():
    try:
        response = requests.get("http://localhost:5000/obtener_nodo1/sumar_su_numero")
        if response.status_code == 200:
            print(response.json()["mensaje"])
            print(f"Sumatoria actual del nodo0: {response.json()['sumatoria_actual_del_nodo0']}")
        else:
            print("Error al obtener y sumar el número del nodo1.")
    except Exception as e:
        print(f"Excepción al obtener y sumar el número del nodo1: {str(e)}")

def ver_sumatoria_actual_nodo1():
    try:
        response = requests.get("http://localhost:5000/obtener_nodo1/sumatoria_actual")
        if response.status_code == 200:
            print(f"Sumatoria actual del nodo1: {response.json()['sumatoria_actual_del_nodo1']}")
        else:
            print("Error al obtener la sumatoria actual del nodo1.")
    except Exception as e:
        print(f"Excepción al obtener la sumatoria actual del nodo1: {str(e)}")

def main():
    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ver_estado_mis_numeros()
            elif opcion == "2":
                ver_estado_numeros_vecinos()
            elif opcion == "3":
                obtener_y_sumar_numero_nodo1()
            elif opcion == "4":
                ver_sumatoria_actual_nodo1()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Volviendo al menú principal.")

if __name__ == "__main__":
    main()

