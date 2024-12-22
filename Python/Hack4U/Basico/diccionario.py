#!/usr/bin/env python3

nombres = {"manzanas":1000, "peras":1500, "naranja": 800, "fresas": 300}

print (type(nombres))

for fruta, precio in nombres.items():
    print (f"Las {fruta} tienen un precio de ${precio:,}".replace(",", "."))
