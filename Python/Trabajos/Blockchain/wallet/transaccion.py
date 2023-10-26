import requests
import json

sender = input("Digite su wallet: ")
recipient = input("Digite la wallet destino: ")
amount = int(input("Digite el monto a enviar: "))

url = 'http://172.17.0.2:5000/transactions/new'

data = {
    "sender": sender,
    "recipient": recipient,
    "amount": amount
}

payload = json.dumps(data)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=payload, headers=headers)

print(response.status_code) 
print(response.text)

