#ejercicio 6

def contar_bloques_iguales(lista, resultado = 0):
    if not lista:
        return resultado

    if len(lista)== 1:
        return resultado + 1
    if lista[0] != lista[1]:
        return contar_bloques_iguales(lista[1:], resultado + 1)
    else:
        return contar_bloques_iguales(lista[1:], resultado)
