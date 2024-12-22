#!/usr/bin/env python3

nombre = "Andrés"
nick = "M0xX"
edad = 21

print (f"Hola, mi nombre es {nombre} mi nick es {nick}.\nActualmente tengo {edad} años")
print ("Hola, mi nombre es {} mi nick es {}. \nActualmente tengo {} años".format(nombre, nick, edad))
print ("Hola, mi nombre es " + nombre + " mi nick es " + str(nick) + ".\nActualmente tengo " + str(edad) + " años")
print ("Hola, mi nombre es %s mi nick es %s.\nActualmente tengo %d años" % (nombre, nick, edad))
print ("\nHola, mi nombre es {0} mi nick es {1}.\nActualmente sigo sieno {0}".format(nombre, nick))
