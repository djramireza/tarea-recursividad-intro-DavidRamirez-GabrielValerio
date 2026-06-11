#E:Un numero entero
#S:Cantidad de digitos pares que tiene

def contar_pares(n):
    if n == 0:
        return 0
    elif (n%10)%2 == 0:
        return 1 + contar_pares(n//10)
    else:
        return 0 + contar_pares(n//10)