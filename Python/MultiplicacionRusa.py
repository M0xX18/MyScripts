def multiplicacion_rusa(multiplicando, multiplicador, num_iteraciones=0):
    if multiplicador != 1:
        num_iteraciones += 1
        multiplicando *= 2
        multiplicador //= 2
        print(f"Iteración {num_iteraciones}: Multiplicando = {multiplicando}, Multiplicador = {multiplicador}")
        return multiplicacion_rusa(multiplicando, multiplicador, num_iteraciones)
    else:
        return num_iteraciones
try:
    multiplicando = int(input("Ingresa el multiplicando: "))
    multiplicador = int(input("Ingresa el multiplicador: "))
except ValueError:
    print("Ingresa numeros enteros!")
num_iteraciones = multiplicacion_rusa(multiplicando, multiplicador)
print("Número de iteraciones:", num_iteraciones)
