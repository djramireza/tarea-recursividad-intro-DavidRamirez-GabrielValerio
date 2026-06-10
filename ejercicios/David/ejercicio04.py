#ejercicio 4

def invertir_numero(num, resultado=0):
    if num == 0:
        return resultado
    if num > 0:
        nuevo = num % 10
        resultado = resultado * 10 + nuevo
    return invertir_numero(num//10, resultado)
        
