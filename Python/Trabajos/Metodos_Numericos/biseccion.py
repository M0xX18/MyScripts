# Codigo Python con el Metodo de Bisección generada por ChatGPT #

def biseccion(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("El teorema de Bolzano no se cumple. Intente con otro intervalo.")
        return None

    iteraciones = 0
    c = a 

    while (b - a) / 2.0 > tol:
        iteraciones += 1
        c = (a + b) / 2.0 
        if f(c) == 0.0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else: 
            a = c

        print(f"Iteración {iteraciones}: a={a}, b={b}, c={c}, f(c)={f(c)}")

    return c

def funcion(x):
    return x**3 - x - 2 

a = 1
b = 2
tol = 1e-6

raiz = biseccion(funcion, a, b, tol)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")

