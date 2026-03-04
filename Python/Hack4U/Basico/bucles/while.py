#!/usr/bin/env python3

lote = 0

manzana = 2

while lote < 120:
    lote += manzana
    print(f"El lote vale = {lote}")
    manzana *= manzana
print(f"La manzana final vale = {manzana}")
