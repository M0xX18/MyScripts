while True:

    try:
        
        nombre = input("Hola! Cual es tu nombre?: ")
        print(f"\nBienvenido {nombre}!")
        edad = int(input("\nCual es tu edad?: "))
        print(f"\nTu edad es {edad}")
        break

    except ValueError:

        print("\nEl tipo de dato es incorrecto\n")
