#!/usr/bin/env python3

import requests

payload = {'parametro1': 'value1', 'parametro2': 'value2', 'parametro3': 'value3'}

response = requests.post("https://httpbin.org/post", data=payload)

print(response.text)
