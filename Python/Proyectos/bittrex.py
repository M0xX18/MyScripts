import requests

# URL del API de Bittrex
url = "https://api.bittrex.com/v3/markets"

# Realiza la solicitud GET al API
response = requests.get(url)

# Comprueba si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Analiza la respuesta JSON
    data = response.json()
    
    # Ahora puedes trabajar con los datos
    for currency in data:
        print("Symbol:", currency["symbol"])
        print("Name:", currency["name"])
        print("Coin Type:", currency["coinType"])
        print("Status:", currency["status"])
        print("Min Confirmations:", currency["minConfirmations"])
        print("Notice:", currency["notice"])
        print("Transaction Fee:", currency["txFee"])
        print("Logo URL:", currency["logoUrl"])
        print("Prohibited In:", currency["prohibitedIn"])
        print("Base Address:", currency["baseAddress"])
        print("Associated Terms of Service:", currency["associatedTermsOfService"])
        print("Tags:", currency["tags"])
        print("\n")
else:
    print("Error en la solicitud. Código de respuesta:", response.status_code)

