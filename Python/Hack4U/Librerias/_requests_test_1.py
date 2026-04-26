#!/usr/bin/env python3

import requests

response = requests.get("https://api.hubapi.com")

if response.status_code == 200:
    print("Yes of course my horse")
else:
    print("No hay sistema")

with open("test.html", "w") as html:
    html.write(response.text)

