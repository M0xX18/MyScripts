def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    if y == 0:
        raise ValueError("No se puede dividir en 0")
    else:
        return x / y
