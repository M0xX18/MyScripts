#!/usr/bin/env python3

import sys

print(f"El argumento numero 1 es {sys.argv[1]}")
print(f"La cantidad total de argumentos es: {sys.argv}")

status_code = 1

print(f"Saliendo con status code {status_code}")

sys.exit(status_code)
