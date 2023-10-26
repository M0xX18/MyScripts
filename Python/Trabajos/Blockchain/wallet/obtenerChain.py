import requests

url = 'http://172.17.0.2:5000/chain'

response = requests.get(url)

if response.status_code == 200:
    chain_data = response.json()
    chain = chain_data['chain']
    length = chain_data['length']

    print(f'Blockchain: {chain}')
    print(f'Longitud de la cadena: {length}')
else:
    print(f'Error: {response.text}')
