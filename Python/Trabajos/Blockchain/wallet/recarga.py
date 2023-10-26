import requests
import json

wallet = input("Digite la wallet a recargar: ")
amount = int(input("Digite el monto de la recarga: "))

url = 'http://172.17.0.2:5000/wallet/recargar'

data = {
    'wallet': wallet,
    'amount': amount
}

payload = json.dumps(data)
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=payload, headers=headers)

print(response.status_code)
print(response.text)
