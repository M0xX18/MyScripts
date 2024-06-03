import requests
import json

def consulta():
    try:
        print("Ejecutando consulta...")

        url_consulta = 'http://172.17.0.2:5000/wallet/saldo'
        wallet_nombre_consulta = input("Digite la direccion de la wallet a consultar: ") 
        params = {'wallet': wallet_nombre_consulta}
        response = requests.get(url_consulta, params=params)

        print(response.status_code)
        print(response.text)

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Volviendo al menú...")

def crearWallet():
    try:
        print("Ejecutando crearWallet...")

        url_crear = 'http://172.17.0.2:5000/wallet/nueva'
        response = requests.post(url_crear)

        print(response.status_code)
        print(response.text)

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Volviendo al menú...")

def obtenerChain():
    try:
        print("Ejecutando obtenerChain...")

        url_obtenerChain = 'http://172.17.0.2:5000/chain'
        response = requests.get(url_obtenerChain)

        if response.status_code == 200:
            chain_data = response.json()
            chain = chain_data['chain']
            length = chain_data['length']

            print(f'Blockchain: {chain}')
            print(f'Longitud de la cadena: {length}')
        else:
            print(f'Error: {response.text}')

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Volviendo al menú...")

def recarga():
    try:
        print("Ejecutando recarga...")
        wallet = input("Digite la wallet a recargar: ")
        amount_recarga = int(input("Digite el monto de la recarga: "))

        url_recarga = 'http://172.17.0.2:5000/wallet/recargar'

        data_recarga = {
            'wallet': wallet,
            'amount': amount_recarga
        }

        payload = json.dumps(data_recarga)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url_recarga, data=payload, headers=headers)

        print(response.status_code)
        print(response.text)

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Volviendo al menú...")

def transaccion():
    try:
        print("Ejecutando transaccion...")
        sender = input("Digite su wallet: ")
        recipient = input("Digite la wallet destino: ")
        amount_Tx = int(input("Digite el monto a enviar: "))

        url_Tx = 'http://172.17.0.2:5000/transactions/new'

        data_Tx = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount_Tx
        }

        payload = json.dumps(data_Tx)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url_Tx, data=payload, headers=headers)

        print(response.status_code) 
        print(response.text)

    except KeyboardInterrupt:
        print("\nInterrupción detectada. Volviendo al menú...")

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Crear Wallet")
        print("2. Consultar saldo")
        print("3. Recargar saldo")
        print("4. Transacción")
        print("5. Obtener Chain")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            crearWallet()
        elif opcion == '2':
            consulta()
        elif opcion == '3':
            recarga()
        elif opcion == '4':
            transaccion()
        elif opcion == '5':
            obtenerChain()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

