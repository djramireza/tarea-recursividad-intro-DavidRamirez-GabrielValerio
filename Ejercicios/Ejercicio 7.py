#E: Numero entero
#S: Una lista con 2 numeros, los digitos pares e impares del numero original

#Del ejercicio 4
def invertir_numero(n):
    return invertir_numero_aux(n, 0)

def invertir_numero_aux(n, res):
    if n == 0:
        return res
    return invertir_numero_aux(n//10, res * 10 + n % 10)

#Cuenta digitos
def contar_dig(n):
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + contar_dig(n//10)


def separar_por_paridad(n):
    return separar_aux(n, 0, 0)

def separar_aux(n, res_p, res_i):
    if n == 0:
        return [invertir_numero(res_p), invertir_numero(res_i)]
    
    ultimo = n % 10
    resto = n // 10

    if ultimo % 2 == 0:
        return separar_aux(resto,(res_p * 10) + ultimo, res_i)
    else:
        return separar_aux(resto, res_p, (res_i * 10) + ultimo)

