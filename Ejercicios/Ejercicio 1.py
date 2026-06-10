#E: Numero entero
#S: Suma de sus digitos

def sumar_digitos(n):
    if n == 0:
        return 0
    return (n%10) + sumar_digitos(n//10)
