def suma(a, b):
    try:
        return a + b
    except Exception as e:
        print(f"{type(e).__name__}: Tipo de dato no válido")

def resta(a, b):
    try:
        return a - b
    except Exception as e:
        print(f"{type(e).__name__}: Tipo de dato no válido")
        

def producto(a, b):
    try:
        return a * b
    except Exception as e:
        print(f"{type(e).__name__}: Tipo de dato no válido")

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"{type(e).__name__}: No es posible dividir entre cero")
    except Exception as e:
        print(f"{type(e).__name__}: Tipo de dato no válido")