#ejercicio 10

def comprimir_repetidos(lista):
    return comprimir_repetidos_aux(lista)

def comprimir_repetidos_aux(lista, resultado = None):

    if resultado is None:
        resultado = []

    if not lista:
        return resultado
    
    num = lista[0]
    contador = 1
    i = 1
    while i < len(lista) and lista[i] == num:
        contador += 1
        i +=1

    resultado.append([num, contador])
    
    return comprimir_repetidos_aux(lista[i:], resultado)
