#!/usr/bin/env python3

info = {"nombre": "Andres", "edad": 22, "hobbies": "Ciberseguridad"}

updated_info = {"Novia": True, "Trabajo": False, "Tiempo": False}

updated_info["Trabajo"] = True

info.update(updated_info)

info["PC"] = "Acer"

print(info.get("nombre"))
print(info.get("edades", "No hay edades"))

print(info)
