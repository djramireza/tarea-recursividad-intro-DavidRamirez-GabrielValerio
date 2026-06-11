#E: Numero entero
#S: Numero sin numeros impares


def cant_digitos(n):
    if n < 10:
        return 1
    return 1 + cant_digitos(n//10)

def eliminar_impares(n):
    return impares_aux(n, 0)

def impares_aux(n, res):
    if n == 0:
        return res
    
    primer_dig = n // (10**(cant_digitos(n)-1))
    resto = n % (10**(cant_digitos(n)-1))

    if primer_dig % 2 == 0:
        return impares_aux(resto, (10*res) + primer_dig)
    else:
        return impares_aux(resto, res)