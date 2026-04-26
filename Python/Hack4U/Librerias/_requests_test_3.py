#!/usr/bin/env python3

import requests

headers = {'User-Agent': '0x27;test--\ -?'}

values = {'Test1': 'Value1'}

response = requests.post("https://httpbin.org/post", headers=headers, params=values)

print(response.text)
