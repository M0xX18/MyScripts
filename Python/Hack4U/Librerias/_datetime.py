#!/usr/bin/env python3

import datetime

ahora = datetime.datetime.now()
fecha = datetime.date(2026, 3, 16)

año = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

periodo = "AM"

if hora >= 12:
    period = "PM"
    hora -= 12

print(f"La fecha registrada es {fecha}\n")

print(f"La fecha acutual es:\nAño: {año}\nMes: {mes}\nDía: {dia}\n\nY la hora es: \n{hora}:{minuto}:{segundo} {periodo}")
