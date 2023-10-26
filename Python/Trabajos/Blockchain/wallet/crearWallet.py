import requests

url = 'http://172.17.0.2:5000/wallet/nueva'

response = requests.post(url)

print(response.status_code)
print(response.text)