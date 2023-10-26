import requests

url = 'http://172.17.0.2:5000/wallet/saldo'


wallet_nombre = input("Digite la direccion de la wallet a consultar: ") 

params = {'wallet': wallet_nombre}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)

