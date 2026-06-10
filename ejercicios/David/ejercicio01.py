#Ejercicio 1

def sumar_digitos(num, resultado = 0):
    return sumar_digitos_aux(num, resultado)


def sumar_digitos_aux(num, resultado):
    if num == 0:
        return resultado
    if num > 0:
            ultimo = num%10
            resultado += ultimo
    return sumar_digitos_aux(num//10, resultado)
